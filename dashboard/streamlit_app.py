import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your merged data
df = pd.read_csv('../data/integrated_weather_energy_health_april_2025_hourly.csv')

st.title("Helsinki Weather, Energy, and Health Dashboard")

st.header("Correlation Matrix")
st.dataframe(df.corr(numeric_only=True).round(2))

st.header("Time Series Plot")
cols = st.multiselect("Variables to Plot", ['temp', 'consumption_kwh', 'emergency_visits'], default=['temp', 'consumption_kwh'])
fig, ax = plt.subplots()
df.set_index('timestamp')[cols].plot(ax=ax, figsize=(12, 4))
st.pyplot(fig)

st.header("Scatter Plot")
x = st.sidebar.selectbox("X axis", ['temp', 'consumption_kwh'])
y = st.sidebar.selectbox("Y axis", ['emergency_visits', 'consumption_kwh', 'temp'])
fig2, ax2 = plt.subplots()
ax2.scatter(df[x], df[y], alpha=0.5)
ax2.set_xlabel(x)
ax2.set_ylabel(y)
st.pyplot(fig2)