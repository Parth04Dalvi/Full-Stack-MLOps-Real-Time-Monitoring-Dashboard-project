# Full Stack MLOps Real Time Monitoring Dashboard project
This project provides a mock API for a real-time anomaly prediction model, designed to be a backend for a full-stack MLOps project. It includes features for real-time prediction, model health monitoring, and historical data reporting.


<img width="1022" height="487" alt="image" src="https://github.com/user-attachments/assets/1c42eb9e-4824-4edc-bbdf-9b2cf28bdae6" />


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



<img width="1135" height="751" alt="image" src="https://github.com/user-attachments/assets/3e4016c1-b68c-4721-9aa0-a3c49cb552e4" />

