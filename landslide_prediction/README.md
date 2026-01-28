# Landslide Prediction System

A software-based digital twin prototype for landslide risk prediction using Machine Learning.

## 📌 Overview

This system simulates environmental sensors (Rainfall, Soil Moisture, Vibration, etc.), processes the data in real-time, feeds it into a Random Forest Classifier, and displays the risk level on a live dashboard.

## 🏗 System Architecture

1. **Sensor Simulator**: Generates synthetic correlated data (Digital Twin).
2. **Backend API (Flask)**: Receives data, pre-processes it, and runs the ML model.
3. **ML Model**: Random Forest Classifier trained on synthetic data.
4. **Dashboard**: Live HTML/JS interface showing sensor values and risk status.

## 🚀 How to Run

Follow these steps to run the entire system.

### 1. Setup Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Prepare Data & Model

Generate the dataset and train the model:

```bash
# Generate data
python landslide_prediction/ml/generate_data.py

# Train model
python landslide_prediction/ml/train_model.py
```

### 3. Start the Backend API

In a new terminal:

```bash
source venv/bin/activate
python landslide_prediction/server/app.py
```

_Server runs on http://localhost:5000_

### 4. Start the Dashboard

In another terminal:

```bash
source venv/bin/activate
python landslide_prediction/dashboard/dashboard.py
```

_Dashboard runs on http://localhost:5001_

### 5. Start the Sensor Simulator

In a third terminal:

```bash
source venv/bin/activate
python landslide_prediction/simulator/sensor_simulator.py
```

_Simulator starts sending data to the backend._

---

## 🧪 Simulation Logic

- **Normal Conditions**: Low rain, stable vibration → **Low Risk (Green)**
- **Heavy Rain**: Increases soil moisture over time → **Moderate Risk (Yellow)**
- **Critical Event**: High Rain + High Moisture + Vibration Shift → **High Risk (Red)**

## ⚠️ Limitations

- **Synthetic Data**: The model is trained on rule-based synthetic data, not real historical geological data.
- **Prototype**: This is for academic demonstration only.
