import json
import random
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(
    title="Real-Time Anomaly Prediction API",
    description="Mock API for a predictive anomaly detection model, designed for a full-stack MLOps project."
)

# CORS middleware setup for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins for development simplicity
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Data Structures (Pydantic Models) ---

class AnomalyPrediction(BaseModel):
    """Schema for a single prediction result."""
    timestamp: str
    feature_value: float
    prediction_score: float
    is_anomaly: bool

class ModelHealth(BaseModel):
    """Schema for monitoring key MLOps metrics."""
    model_version: str
    last_trained: str
    accuracy: float
    data_drift_metric: float
    serving_status: str

# --- Mock Data Generation ---

def generate_prediction():
    """Generates a mock real-time prediction point."""
    now_str = datetime.now().isoformat()
    
    # 90% chance of normal behavior
    is_anomaly = random.random() < 0.1
    
    if is_anomaly:
        # High value/score for anomaly
        feature_value = round(random.uniform(90, 110), 2)
        prediction_score = round(random.uniform(0.7, 0.99), 4)
    else:
        # Normal value/score
        feature_value = round(random.uniform(40, 60), 2)
        prediction_score = round(random.uniform(0.1, 0.4), 4)

    return AnomalyPrediction(
        timestamp=now_str,
        feature_value=feature_value,
        prediction_score=prediction_score,
        is_anomaly=is_anomaly
    )

# Static mock health data (showcases versioning, a key MLOps component)
MOCK_MODEL_HEALTH = ModelHealth(
    model_version="v2.1.3",
    last_trained="2025-11-10T14:30:00Z",
    accuracy=0.975,
    data_drift_metric=0.15, # Anything > 0.2 might be flagged
    serving_status="Healthy"
)

# --- API Endpoints ---

@app.get("/", summary="Root Health Check")
def read_root():
    """Simple health check endpoint."""
    return {"status": "ok", "service": "Anomaly Detection API"}

@app.get("/predict", response_model=AnomalyPrediction, summary="Get Real-Time Prediction")
def get_prediction():
    """
    Returns a single, real-time prediction from the mocked model.
    The data simulates a sensor reading and an anomaly probability score.
    """
    return generate_prediction()

@app.get("/health", response_model=ModelHealth, summary="Get MLOps Model Health Metrics")
def get_health():
    """
    Returns mock metrics that would typically be logged by MLflow or a custom monitoring tool,
    demonstrating the MLOps component.
    """
    return MOCK_MODEL_HEALTH

# Example of a Dockerfile/GCP-ready structure for the README.md:
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

# To run this: pip install uvicorn fastapi pydantic. Then: uvicorn app:app --reload
