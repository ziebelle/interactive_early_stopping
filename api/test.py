import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import EarlyStopping as es

import scipy
from scipy import sparse
from scipy.sparse import dia_matrix

sample_size = 1000
indices = np.arange(sample_size) + 1

signal_supersmooth = 5 * np.exp(-0.1 * indices)
signal_smooth = 5000 * np.abs(np.sin(0.01 * indices)) * indices ** (-1.6)
signal_rough = 250 * np.abs(np.sin(0.002 * indices)) * indices ** (-0.8)

true_signal = signal_rough

true_noise_level = 0.01
noise = true_noise_level * np.random.normal(0, 1, sample_size)

eigenvalues = 1 / np.sqrt(indices)
design = dia_matrix(np.diag(eigenvalues))

response = eigenvalues * true_signal + noise

alg = es.Landweber(design, response, learning_rate=1, true_signal=true_signal, true_noise_level=true_noise_level)

# Initialize Landweber class
critical_value = sample_size * true_noise_level**2
discrepancy_time = alg.get_discrepancy_stop(critical_value, 3000)

result = discrepancy_time