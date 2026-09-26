import os
import joblib
from src.data_fetcher import fetch_weather
from src.forecasting import train_temperature_model

CITY = "Kolkata"

hourly, daily, meta = fetch_weather(CITY, forecast_days=7)

os.makedirs("data", exist_ok=True)
hourly.to_csv("data/weather_hourly.csv", index=False)
daily.to_csv("data/weather_daily.csv", index=False)

try:
    model, features, metrics = train_temperature_model(hourly)
    os.makedirs("models", exist_ok=True)
    joblib.dump(
        {
            "model": model,
            "features": features,
            "metrics": metrics,
            "city": CITY,
        },
        "models/temperature_model.joblib",
    )
    print("Model metrics:", metrics)
    print("Saved models/temperature_model.joblib")
except Exception as exc:
    print("Training skipped:", exc)
