# 🌦️ Weather Forecasting System

An end-to-end Data Science project for weather analytics and temperature forecasting.

## Features
- City search with geocoding
- Live weather retrieval through Open-Meteo
- 1–7 day forecast dashboard
- Temperature, precipitation, humidity and wind analysis
- Exploratory Data Analysis
- Random Forest temperature forecasting baseline
- Interactive Plotly charts
- Streamlit dashboard

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, Requests, Plotly, Streamlit, Matplotlib, Seaborn, Joblib

## Structure
```
weather-forecasting-system/
├── data/
├── models/
├── notebooks/
│   └── weather_analysis.py
├── src/
│   ├── data_fetcher.py
│   └── forecasting.py
├── app.py
├── train.py
├── requirements.txt
└── README.md
```

## Run locally
```bash
pip install -r requirements.txt
python train.py
streamlit run app.py
```

The application uses Open-Meteo for weather data. The forecasting model is an educational portfolio baseline and is not an authoritative weather service.
