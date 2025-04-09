# Interactive Computation Demo

This project demonstrates integration between a Vue.js frontend and a FastAPI Python backend for interactive computation.

## Features

- Interactive slider to set input value
- Python backend for performing computations
- Real-time display of computation results

## Project Structure

```
/
├── app.vue               # Vue.js frontend
├── api/                  # Python backend
│   ├── main.py           # FastAPI application
│   └── run.py            # Server runner
├── requirements.txt      # Python dependencies
└── package.json          # Node.js dependencies
```

## Setup and Running

### 1. Python Backend (FastAPI)

1. Set up a Python virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```
   cd api
   python run.py
   ```
   The API will be available at http://localhost:8000

### 2. Vue.js Frontend

1. Install Node.js dependencies:
   ```
   npm install
   ```

2. Run the development server:
   ```
   npm run dev
   ```
   The frontend will be available at http://localhost:3000

## API Endpoints

- `GET /`: Health check endpoint
- `POST /compute`: Accepts a JSON body with a `value` field and returns a computation result

## How It Works

1. Set a value using the slider in the frontend
2. Click "Compute" to send the value to the FastAPI backend
3. The backend processes the value (squares it and adds 10)
4. The result is displayed on the frontend
