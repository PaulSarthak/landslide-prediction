from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

# Backend API URL
BACKEND_URL = "http://localhost:5000/api/status"

@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(port=5001, debug=True)
