from flask import Flask, request, jsonify
import pickle
import numpy as np
import os
import sys

# Ensure we can find the model
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../ml/model.pkl')

app = Flask(__name__)

# Global state to store the latest reading and prediction
current_state = {
    "rainfall": 0,
    "soil_moisture": 0,
    "vibration": 0,
    "humidity": 0,
    "temperature": 0,
    "risk_level": "Unknown",
    "risk_code": -1
}

model = None

def load_model():
    global model
    try:
        if os.path.exists(MODEL_PATH):
            with open(MODEL_PATH, 'rb') as f:
                model = pickle.load(f)
            print("Model loaded successfully.")
        else:
            print(f"Model not found at {MODEL_PATH}. Prediction will fail.")
            model = None
    except Exception as e:
        print(f"Error loading model: {e}")
        model = None

def get_risk_label(code):
    if code == 0: return "Low"
    if code == 1: return "Moderate"
    if code == 2: return "High"
    return "Unknown"

@app.route('/api/sensor-data', methods=['POST'])
def receive_sensor_data():
    global current_state, model
    
    if model is None:
        load_model()
        
    data = request.json
    
    # Extract features in the correct order for the model
    # Features: rainfall, soil_moisture, vibration, humidity, temperature
    try:
        features = [
            data.get('rainfall', 0),
            data.get('soil_moisture', 0),
            data.get('vibration', 0),
            data.get('humidity', 0),
            data.get('temperature', 0)
        ]
        
        # Predict
        risk_code = -1
        risk_level = "Unknown"
        
        if model:
            prediction = model.predict([features])
            risk_code = int(prediction[0])
            risk_level = get_risk_label(risk_code)
        
        # Update state
        current_state = {
            **data,
            "risk_level": risk_level,
            "risk_code": risk_code
        }
        
        print(f"Received: {data} -> Risk: {risk_level}")
        
        return jsonify(current_state)
        
    except Exception as e:
        print(f"Error processing data: {e}")
        return jsonify({"error": str(e)}), 400

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify(current_state)

if __name__ == '__main__':
    load_model()
    app.run(port=5000, debug=True)
