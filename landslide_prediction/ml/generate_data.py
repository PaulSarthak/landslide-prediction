import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

def generate_data(num_samples=1000):
    data = []
    
    for _ in range(num_samples):
        # Generate random base values
        # Rainfall: 0 to 100 mm/h
        rainfall = np.random.uniform(0, 100)
        
        # Soil Moisture: correlated with rainfall
        # Base moisture + effect of rainfall + random noise
        soil_moisture = np.random.uniform(10, 60) + (rainfall * 0.4) + np.random.normal(0, 5)
        soil_moisture = np.clip(soil_moisture, 0, 100)
        
        # Vibration: 0 to 1 (normalized) based on "seismic activity" or loose soil
        # Occasional high vibration spikes
        vibration = np.random.exponential(0.1)
        vibration = np.clip(vibration, 0, 1)
        
        # Humidity: 30% to 100%
        humidity = np.random.uniform(30, 90) + (rainfall * 0.1)
        humidity = np.clip(humidity, 30, 100)
        
        # Temperature: 10C to 40C
        temperature = np.random.uniform(15, 35) - (rainfall * 0.05)
        
        # Determine Risk Label based on rules
        # Risk 0: Low, 1: Moderate, 2: High
        risk = 0
        
        # Rule-based Logic
        # High Risk: Heavy rain AND High Moisture OR Significant Vibration
        if (rainfall > 50 and soil_moisture > 70) or (vibration > 0.4) or (rainfall > 80):
            risk = 2
        # Moderate Risk: Moderate rain OR Moderate Moisture
        elif (rainfall > 20 and soil_moisture > 40) or (rainfall > 30):
            risk = 1
        else:
            risk = 0
            
        data.append({
            "rainfall": round(rainfall, 2),
            "soil_moisture": round(soil_moisture, 2),
            "vibration": round(vibration, 4),
            "humidity": round(humidity, 2),
            "temperature": round(temperature, 2),
            "risk": risk
        })
        
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = generate_data(1000)
    output_path = "landslide_prediction/data/landslide_data.csv"
    df.to_csv(output_path, index=False)
    print(f"Generated {len(df)} samples saved to {output_path}")
    print(df["risk"].value_counts())
