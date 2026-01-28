import time
import random
import requests
import json
import math

SERVER_URL = "http://localhost:5000/api/sensor-data"
INTERVAL = 2  # seconds between readings

def generate_sensor_data(t):
    """
    Generate realistic correlated sensor data based on a time step t.
    We use sine waves to simulate day/night cycles or weather patterns
    to vary the "base" conditions, and then apply correlations.
    """
    
    # Simulate a weather cycle (e.g. valid "storms" come and go)
    # This factor oscillates between 0 and 1
    weather_cycle = (math.sin(t * 0.1) + 1) / 2
    
    # Rainfall: Spiky, depends on weather cycle
    # If weather_cycle is high, chance of heavy rain
    rainfall_base = 0
    if weather_cycle > 0.7:
        rainfall_base = random.uniform(20, 100)
    elif weather_cycle > 0.4:
        rainfall_base = random.uniform(0, 30)
    
    rainfall = rainfall_base + random.normalvariate(0, 2)
    rainfall = max(0, rainfall)
    
    # Soil Moisture: Reacts to rainfall (with some "memory" or lag conceptually, 
    # but here we simplify to direct correlation + base)
    # Higher rain -> Higher moisture
    base_moisture = 30
    soil_moisture = base_moisture + (rainfall * 0.5) + (weather_cycle * 20) + random.normalvariate(0, 2)
    soil_moisture = max(0, min(100, soil_moisture))
    
    # Humidity: High when raining
    base_humidity = 40
    humidity = base_humidity + (rainfall * 0.3) + random.normalvariate(0, 5)
    humidity = max(0, min(100, humidity))
    
    # Vibration: Usually low, but occasional spikes simulating "events"
    # We can inject a "vibration spike" randomly
    is_quake = random.random() > 0.95
    if is_quake:
        vibration = random.uniform(0.4, 0.9)
    else:
        vibration = random.uniform(0.01, 0.1)
        
    # Temperature: Drops when raining
    base_temp = 25
    temperature = base_temp - (rainfall * 0.1) + random.normalvariate(0, 1)
    
    return {
        "rainfall": round(rainfall, 2),
        "soil_moisture": round(soil_moisture, 2),
        "vibration": round(vibration, 4),
        "humidity": round(humidity, 2),
        "temperature": round(temperature, 1)
    }

def main():
    print(f"Starting Sensor Simulator... Sending data to {SERVER_URL}")
    t = 0
    while True:
        data = generate_sensor_data(t)
        
        try:
            response = requests.post(SERVER_URL, json=data)
            if response.status_code == 200:
                print(f"[SENT] {data} -> {response.json()}")
            else:
                print(f"[ERROR] Server returned {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"[FAIL] Could not connect to {SERVER_URL}. Is the backend running?")
        
        time.sleep(INTERVAL)
        t += 1

if __name__ == "__main__":
    main()
