# Full-Stack-MLOps-Real-Time-Monitoring-Dashboard-project
📉 Real-Time Predictive Anomaly Detection System (Full-Stack MLOps Demo)

Project Overview

This project showcases an end-to-end MLOps pipeline for a critical business function: real-time anomaly detection. It demonstrates proficiency across the full stack—from a containerized Python/FastAPI machine learning model backend to a responsive HTML/JavaScript (Chart.js/Tailwind CSS) dashboard used for real-time monitoring and model health tracking.

The system simulates a scenario (e.g., monitoring a server, IoT sensor, or financial transaction stream) where key metrics are constantly analyzed to flag anomalous behavior.

🔑 Key Features Demonstrated

Full-Stack Development: Interfacing a modern frontend (HTML/Tailwind/JS) with a high-performance Python backend (FastAPI).

MLOps & Model Governance: Tracking core model performance metrics (accuracy, data drift) and managing versions, simulating real-world MLOps practices (like those enforced by tools such as MLflow or DVC).

Real-Time Data Streaming: Using continuous polling and Chart.js to visualize live predictions and feature data.

DevOps Readiness: The Python API is structured for easy containerization using Docker and deployment to cloud platforms (AWS, GCP, or Azure).

🛠️ Technology Stack

Layer

Technology

Rationale & Project Context

Backend/API

Python, FastAPI, Pydantic

Used for high-speed, asynchronous serving of the machine learning model predictions. Pydantic ensures data validation for reliable API contracts.

Model

Python (Mocked)

Simulates a lightweight time-series anomaly model (e.g., Isolation Forest or LSTM) that outputs a probability score.

Frontend/UI

HTML5, Tailwind CSS, Vanilla JS

Focuses on speed and clean, responsive UI design. Tailwind CSS is used for rapid, utility-first styling.

Visualization

Chart.js

Used to render the real-time feature values and anomaly scores, dynamically updated via JavaScript.

Deployment

Docker (Ready)

The API is ready to be containerized, demonstrating production deployment skills.

🏗️ Architecture and Data Flow

Model Simulation (app.py): The FastAPI application exposes two main endpoints:

/predict: Generates mock feature data and an anomaly probability score.

/health: Returns static metadata like model_version, accuracy, and data_drift_metric, which represent key MLOps artifacts.

Frontend Interface (index.html):

The JavaScript layer continuously polls the /predict endpoint every 2 seconds.

It updates the live line chart (Feature Value vs. Anomaly Score) with new data points.

It renders the model health metrics pulled from the /health endpoint, highlighting the production status.

Anomaly Alert: If the prediction score exceeds a high threshold (simulated by the random generator), the frontend triggers a visual pulse animation and changes the status panel to red, demanding immediate attention.

🚀 How to Run the Project

Prerequisites

You must have Python 3.8+ installed.

1. Backend Setup (app.py)

Install Dependencies:

pip install uvicorn fastapi pydantic


Run the API Server:

uvicorn app:app --reload


The API will be available at http://127.0.0.1:8000.

2. Frontend Access (index.html)

Open the Dashboard: Simply open the index.html file in any modern web browser.

Start Monitoring: The dashboard automatically starts polling the running FastAPI backend and visualizing the live prediction stream.

💡 Future MLOps & System Enhancements

This project is designed to be easily extendable into a production MLOps system:

Real Model Integration: Replace the generate_prediction() function with actual model inference logic (e.g., loading a pre-trained PyTorch or TensorFlow model).

Database Integration: Implement persistent storage (e.g., PostgreSQL or MongoDB) to log prediction history, enhancing auditability and trend analysis.

Data Versioning: Integrate tools like DVC to version data and models alongside the codebase, ensuring full reproducibility.

Deployment Pipeline: Create a comprehensive Dockerfile and a GitHub Actions workflow to automate testing, building, and pushing the container to a cloud registry.
