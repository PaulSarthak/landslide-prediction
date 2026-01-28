from flask import Flask, render_template, jsonify, request
import requests
import os

app = Flask(__name__)

# Backend API URL
BACKEND_URL = "http://localhost:8000/api/status"

import socket

@app.route('/')
def index():
    try:
        # Get local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except:
        local_ip = "localhost"
        
    control_url = f"http://{local_ip}:8001/control"
    return render_template('index.html', control_url=control_url)

@app.route('/data')
def get_data():
    try:
        response = requests.get(BACKEND_URL)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Backend Error"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/control')
def control():
    return render_template('control.html')

@app.route('/api/update', methods=['POST'])
def update_sensor():
    try:
        data = request.json
        # Forward to Backend API
        response = requests.post("http://localhost:8000/api/sensor-data", json=data)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    import threading
    import webbrowser
    import time
    
    def open_browser():
        time.sleep(1) # Wait for server to start
        webbrowser.open('http://localhost:8001')
        
    threading.Thread(target=open_browser).start()
    app.run(host='0.0.0.0', port=8001, debug=True)
