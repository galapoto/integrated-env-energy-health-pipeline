import pandas as pd

# Read the CSV with semicolon separator
df = pd.read_csv('../data/finland_energy_consumption_april_2025.csv', sep=';')

# Rename columns for easier access
df = df.rename(columns={
    "startTime": "start_time",
    "endTime": "end_time",
    "Electricity consumption in Finland": "consumption_mwh"
})

# Convert consumption to kWh
df['consumption_kwh'] = df['consumption_mwh'] * 1000

# Convert start_time to pandas datetime
df['start_time'] = pd.to_datetime(df['start_time'])

# Set to hourly by resampling: sum 4 quarters per hour
df = df.set_index('start_time')
hourly = df['consumption_kwh'].resample('H').sum().reset_index()

# Save in the expected format
hourly[['start_time', 'consumption_kwh']].to_csv('../data/finland_energy_consumption_april_2025_hourly.csv', index=False)

print("Hourly energy data in kWh saved to ../data/finland_energy_consumption_april_2025_hourly.csv")