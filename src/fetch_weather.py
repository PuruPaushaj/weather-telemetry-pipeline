import requests
import os
import json
from datetime import datetime

# API endpoint
API_URL = "https://api.open-meteo.com/v1/forecast"

# Example: coordinates for New York (you can change later)
LAT, LON = 40.7128, -74.0060

# Parameters for hourly weather data
params = {
    "latitude": LAT,
    "longitude": LON,
    "hourly": ["temperature_2m", "relative_humidity_2m", "windspeed_10m"],
    "forecast_days": 1,
    "timezone": "auto"
}

# Output folder
RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

# File name with timestamp
timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
filename = os.path.join(RAW_DIR, f"weather_{timestamp}.json")

def fetch_weather():
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"✅ Weather data saved to {filename}")
    else:
        print(f"❌ Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    fetch_weather()

