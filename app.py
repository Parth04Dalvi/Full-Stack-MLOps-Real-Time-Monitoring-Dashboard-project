import json
import random
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

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

class ReportData(BaseModel):
    """Schema for historical report data."""
    id: int
    timestamp: str
    severity: str
    description: str


# --- Mock Data Generation ---

def generate_prediction():
    """Generates a mock real-time prediction point."""
    now_str = datetime.now().isoformat()
    
    # 10% chance of anomaly
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

def generate_reports() -> List[ReportData]:
    """Generates a list of mock historical anomaly reports."""
    reports = []
    now = datetime.now()
    for i in range(5):
        report_time = now - timedelta(days=random.randint(1, 30), hours=random.randint(1, 23))
        severity = random.choice(["High", "Medium", "Low"])
        description = f"Anomaly detected on sensor group {chr(random.randint(65, 70))} with severity: {severity}"
        reports.append(ReportData(id=i+1, timestamp=report_time.isoformat(), severity=severity, description=description))
    return reports

# Static mock health data
MOCK_MODEL_HEALTH = ModelHealth(
    model_version="v3.0.0",
    last_trained="2026-01-15T10:00:00Z",
    accuracy=0.98,
    data_drift_metric=0.12,
    serving_status="Healthy"
)

# --- API Endpoints ---

@app.get("/", summary="Root Health Check")
def read_root():
    """Simple health check endpoint."""
    return {"status": "ok", "service": "Anomaly Detection API"}

@app.get("/predict", response_model=AnomalyPrediction, summary="Get Real-Time Prediction")
def get_prediction():
    """Returns a single, real-time prediction from the mocked model."""
    return generate_prediction()

@app.get("/health", response_model=ModelHealth, summary="Get MLOps Model Health Metrics")
def get_health():
    """Returns mock metrics for the MLOps dashboard."""
    return MOCK_MODEL_HEALTH

@app.get("/reports", response_model=List[ReportData], summary="Get Historical Anomaly Reports")
def get_reports():
    """Returns a list of mock historical anomaly reports."""
    return generate_reports()
