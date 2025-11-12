# Real-Time Anomaly Prediction API

This project provides a mock API for a real-time anomaly prediction model, designed to be a backend for a full-stack MLOps project. It includes features for real-time prediction, model health monitoring, and historical data reporting.

## Features

- **Real-Time Predictions**: Get anomaly predictions in real-time.
- **Model Health Monitoring**: Monitor key MLOps metrics like model version, accuracy, and data drift.
- **Historical Reports**: Fetch historical anomaly reports.
- **Dark Mode**: A sleek, modern UI with dark mode support.
- **Interactive Charts**: Visualize real-time data with interactive charts.

## API Endpoints

- `GET /`: Health check endpoint.
- `GET /predict`: Get a real-time anomaly prediction.
- `GET /health`: Get model health metrics.
- `GET /reports`: Get historical anomaly reports.

## Running the Project

1. **Install Dependencies**

   ```
   pip install uvicorn fastapi pydantic
   ```

2. **Run the API**

   ```
   uvicorn app:app --reload
   ```

## Frontend

The frontend is a single `index.html` file that uses Tailwind CSS for styling and Chart.js for data visualization. It communicates with the backend API to display real-time data and model health metrics.
