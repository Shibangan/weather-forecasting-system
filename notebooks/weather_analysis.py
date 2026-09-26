import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

hourly = pd.read_csv("../data/weather_hourly.csv", parse_dates=["time"])
daily = pd.read_csv("../data/weather_daily.csv", parse_dates=["time"])

print(hourly.head())
print(hourly.describe())
print(hourly.isna().sum())

plt.figure(figsize=(12, 5))
sns.lineplot(data=hourly, x="time", y="temperature_2m")
plt.title("Hourly Temperature Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(hourly["temperature_2m"], kde=True)
plt.title("Temperature Distribution")
plt.show()

correlation = hourly.select_dtypes("number").corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, fmt=".2f")
plt.title("Weather Variable Correlation")
plt.show()
