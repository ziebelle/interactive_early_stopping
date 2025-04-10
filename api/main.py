from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import EarlyStopping as es

import scipy
from scipy.sparse import dia_matrix

import traceback
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SliderData(BaseModel):
    value: float


@app.get("/")
def read_root():
    return {"message": "FastAPI server is running"}


@app.post("/compute")
async def compute(data: SliderData):
    """
    Performs a simple computation based on the slider value.
    For this example, we'll square the value and add 10.
    """
    try:
        logger.info(f"Received computation request with value: {data.value}")
        sample_size = 1000
        indices = np.arange(sample_size) + 1

        signal_supersmooth = 5 * np.exp(-0.1 * indices)
        signal_smooth = 5000 * np.abs(np.sin(0.01 * indices)) * indices ** (-1.6)
        signal_rough = 250 * np.abs(np.sin(0.002 * indices)) * indices ** (-0.8)

        true_signal = signal_rough

        true_noise_level = data.value
        noise = true_noise_level * np.random.normal(0, 1, sample_size)

        eigenvalues = 1 / np.sqrt(indices)
        design = dia_matrix(np.diag(eigenvalues))

        response = eigenvalues * true_signal + noise

        alg = es.Landweber(
            design, response, learning_rate=1, true_signal=true_signal, true_noise_level=true_noise_level
        )

        # Initialize Landweber class
        critical_value = sample_size * true_noise_level**2
        discrepancy_time = alg.get_discrepancy_stop(critical_value, 3000)
        residuals = alg.residuals

        result = discrepancy_time

        # Convert numpy array to list for JSON serialization
        residuals_list = residuals.tolist() if isinstance(residuals, np.ndarray) else []

        return {"original": data.value, "computed": result, "residuals": residuals_list}
    except Exception as e:
        error_details = traceback.format_exc()
        logger.error(f"Unhandled exception: {str(e)}\n{error_details}")
        raise HTTPException(status_code=500, detail=f"Error during computation: {str(e)}")
