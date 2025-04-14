import requests

from dotenv import load_dotenv
import os
load_dotenv()

WEATHER_API_KEY = os.getenv("OPENWEATHER")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# coords of Chennai
lat = 13.0843
lon = 80.2705

air_pollution_url = f"http://api.openweathermap.org/data/2.5/air_pollution"
params = {
    'lat':lat,
    'lon':lon,
    'appid':WEATHER_API_KEY,
    'units':'metric'
}

air_pollution_response = requests.get(air_pollution_url, params=params)
air_pollution_data = air_pollution_response.json()
air_pollution_data = air_pollution_data['list'][0]


from datetime import datetime
timestamp = datetime.fromtimestamp(air_pollution_data['dt']).strftime('%Y-%m-%d %H:%M:%S') # Convert epoch timestamp to standard format

message = f"""
Air Quality Update 🌍:
- Overall AQI: {air_pollution_data['main']['aqi']}
- Components:
  • CO (Carbon Monoxide): {air_pollution_data['components']['co']} µg/m³
  • NO (Nitric Oxide): {air_pollution_data['components']['no']} µg/m³
  • NO2 (Nitrogen Dioxide): {air_pollution_data['components']['no2']} µg/m³
  • O3 (Ozone): {air_pollution_data['components']['o3']} µg/m³
  • SO2 (Sulfur Dioxide): {air_pollution_data['components']['so2']} µg/m³
  • PM2.5 (Fine Particles): {air_pollution_data['components']['pm2_5']} µg/m³
  • PM10 (Coarse Particles): {air_pollution_data['components']['pm10']} µg/m³
  • NH3 (Ammonia): {air_pollution_data['components']['nh3']} µg/m³

Timestamp: {timestamp}
"""

telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message
}
requests.post(telegram_url, data=payload)