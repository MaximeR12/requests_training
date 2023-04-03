import streamlit as st
import pandas as pd

df = pd.read_csv("openweather/weather_data_fr_20.csv")

st.write(f"""
    Weather data for the 20 most populated french cities
""", df)