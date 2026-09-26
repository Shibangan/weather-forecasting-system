import requests
import pandas as pd

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

def geocode_city(city: str):
    response = requests.get(
        GEOCODING_URL,
        params={"name": city, "count": 1, "language": "en", "format": "json"},
        timeout=20,
    )
    response.raise_for_status()
    results = response.json().get("results", [])
    if not results:
        raise ValueError(f"City not found: {city}")
    result = results[0]
    return result["latitude"], result["longitude"], result.get("name", city), result.get("country", "")

def fetch_weather(city: str, forecast_days: int = 7):
    lat, lon, name, country = geocode_city(city)
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max",
        "forecast_days": forecast_days,
        "timezone": "auto",
    }
    response = requests.get(FORECAST_URL, params=params, timeout=20)
    response.raise_for_status()
    data = response.json()

    hourly = pd.DataFrame(data["hourly"])
    hourly["time"] = pd.to_datetime(hourly["time"])

    daily = pd.DataFrame(data["daily"])
    daily["time"] = pd.to_datetime(daily["time"])

    meta = {"name": name, "country": country, "latitude": lat, "longitude": lon}
    return hourly, daily, meta
