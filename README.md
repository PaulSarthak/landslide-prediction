# Landslide Prediction System

A software-based digital twin prototype for landslide risk prediction using Machine Learning.

## 📌 Overview

This system simulates environmental sensors (Rainfall, Soil Moisture, Vibration, etc.), processes the data in real-time, feeds it into a Random Forest Classifier, and displays the risk level on a live dashboard.

## 🏗 System Architecture

1. **Sensor Simulator**: Generates synthetic correlated data (Digital Twin).
2. **Backend API (Flask)**: Receives data, pre-processes it, and runs the ML model.
3. **ML Model**: Random Forest Classifier trained on synthetic data.
4. **Dashboard**: Live HTML/JS interface showing sensor values and risk status.

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/PaulSarthak/landslide-prediction.git
cd landslide-prediction
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r landslide_prediction/requirements.txt
```

---

## 🏃‍♂️ How to Run

### Step 1: Generate Data & Train Model

First, generate the synthetic dataset and train the Random Forest model.

```bash
# Generate data
python landslide_prediction/ml/generate_data.py

# Train model
python landslide_prediction/ml/train_model.py
```

_This will create `model.pkl` in the `ml/` directory._

### Step 2: Start the Backend Server

This service hosts the API and the ML Model.

```bash
python landslide_prediction/server/app.py
```

_Server runs on http://localhost:5000_

### Step 3: Start the Dashboard

Open a new terminal, activate venv, and run:

```bash
python landslide_prediction/dashboard/dashboard.py
```

_Dashboard runs on http://localhost:5001_

---

## 🎮 Simulation Modes

### Mode A: Automatic Digital Twin (Default)

Run the sensor simulator to generate automatic, realistic environmental data.

```bash
python landslide_prediction/simulator/sensor_simulator.py
```

### Mode B: Manual Control Panel 🎛

If you want to manually test specific landslide conditions:

1. Ensure the **Dashboard** is running.
2. Open your browser to: **[http://localhost:5001/control](http://localhost:5001/control)**
3. Use the sliders to adjust Rainfall, Moisture, and Vibration.
4. Watch the main Dashboard ([http://localhost:5001](http://localhost:5001)) update in real-time!

**Triggering a Landslide Alert:**

- Try setting **Rainfall > 80**
- OR **Rainfall > 50** AND **Soil Moisture > 70**

---

## ⚠️ Notes

- The system defaults to **Low Risk**.
- **Moderate Risk** (Yellow) occurs with elevated rainfall.
- **High Risk** (Red) occurs with extreme conditions or seismic vibration.
- This is an academic prototype.

## 📱 Mobile Control (Bonus)

You can control the simulator from your phone while watching the dashboard on your laptop!

1. Ensure your phone and laptop are on the **same Wi-Fi**.
2. Stop and Restart the **Server** and **Dashboard** (Ctrl+C and run again).
3. Find your laptop's IP address (e.g., `10.3.153.133`).
4. On your phone browser, go to:
   `http://<YOUR_LAPTOP_IP>:5001/control`
   _(Example: http://10.3.153.133:5001/control)_

Now move the sliders on your phone and watch the laptop screen update instantly! 🤯
