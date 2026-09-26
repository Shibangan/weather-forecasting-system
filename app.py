import streamlit as st
import plotly.express as px
from src.data_fetcher import fetch_weather

st.set_page_config(
    page_title="Weather Forecasting System",
    page_icon="🌦️",
    layout="wide",
)

st.title("🌦️ Weather Forecasting System")
st.caption("Interactive weather analytics and forecasting dashboard")

city = st.sidebar.text_input("Enter city", "Kolkata")
forecast_days = st.sidebar.slider("Forecast days", 1, 7, 7)

if st.sidebar.button("Load Weather", type="primary"):
    try:
        st.session_state["weather"] = fetch_weather(city, forecast_days)
    except Exception as exc:
        st.error(f"Unable to load weather: {exc}")

if "weather" not in st.session_state:
    st.info("Enter a city and click **Load Weather**.")
    st.stop()

hourly, daily, meta = st.session_state["weather"]

st.subheader(f"{meta['name']}, {meta['country']}")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Today's Max", f"{daily.iloc[0]['temperature_2m_max']:.1f} °C")
c2.metric("Today's Min", f"{daily.iloc[0]['temperature_2m_min']:.1f} °C")
c3.metric("Rain", f"{daily.iloc[0]['precipitation_sum']:.1f} mm")
c4.metric("Max Wind", f"{daily.iloc[0]['wind_speed_10m_max']:.1f} km/h")

fig_temp = px.line(
    daily,
    x="time",
    y=["temperature_2m_max", "temperature_2m_min"],
    markers=True,
    title="Temperature Forecast",
)
st.plotly_chart(fig_temp, use_container_width=True)

fig_rain = px.bar(
    daily,
    x="time",
    y="precipitation_sum",
    title="Daily Precipitation",
)
st.plotly_chart(fig_rain, use_container_width=True)

fig_hourly = px.line(
    hourly,
    x="time",
    y="temperature_2m",
    title="Hourly Temperature",
)
st.plotly_chart(fig_hourly, use_container_width=True)

st.subheader("Forecast Data")
st.dataframe(daily, use_container_width=True)
