import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

BASE_FEATURES = [
    "temperature_2m",
    "relative_humidity_2m",
    "precipitation",
    "wind_speed_10m",
]

def add_lag_features(df):
    data = df.copy().sort_values("time")
    for lag in [1, 2, 3, 6, 12, 24]:
        data[f"temperature_2m_lag_{lag}"] = data["temperature_2m"].shift(lag)

    data["hour"] = data["time"].dt.hour
    data["dayofyear"] = data["time"].dt.dayofyear
    data["sin_hour"] = np.sin(2 * np.pi * data["hour"] / 24)
    data["cos_hour"] = np.cos(2 * np.pi * data["hour"] / 24)
    return data

def train_temperature_model(df):
    data = add_lag_features(df).dropna()

    features = BASE_FEATURES + [
        "temperature_2m_lag_1", "temperature_2m_lag_2",
        "temperature_2m_lag_3", "temperature_2m_lag_6",
        "temperature_2m_lag_12", "temperature_2m_lag_24",
        "hour", "dayofyear", "sin_hour", "cos_hour",
    ]

    split = int(len(data) * 0.8)
    train, test = data.iloc[:split], data.iloc[split:]

    model = RandomForestRegressor(
        n_estimators=250,
        random_state=42,
        min_samples_leaf=2,
        n_jobs=-1,
    )
    model.fit(train[features], train["temperature_2m"])

    predictions = model.predict(test[features])
    mae = mean_absolute_error(test["temperature_2m"], predictions)
    rmse = np.sqrt(mean_squared_error(test["temperature_2m"], predictions))

    return model, features, {"MAE": mae, "RMSE": rmse}
