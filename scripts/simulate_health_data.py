import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set the time range: April 2025, hourly
start_date = datetime(2025, 4, 1, 0)
end_date = datetime(2025, 5, 1, 0)
date_range = pd.date_range(start=start_date, end=end_date, freq='H', inclusive='left')

# Simulate health data: Emergency visits per hour
# Let's make the base rate higher at night (e.g., more ER cases after 20:00)
hourly = date_range.hour

base_rate = 8                             # Typical hourly average
night_boost = (hourly >= 20) | (hourly < 6)  # True if hour is night
visits = base_rate + night_boost * 5      # Add 5 more cases at night
randomness = np.random.normal(0, 2, len(date_range))  # Some noise

sim_visits = np.round(visits + randomness).astype(int)
sim_visits[sim_visits < 0] = 0  # No negative cases

# Create dataframe
df = pd.DataFrame({
    'timestamp': date_range,
    'emergency_visits': sim_visits
})

output_path = '../data/helsinki_health_emergency_april_2025_hourly.csv'
df.to_csv(output_path, index=False)
print(f"Simulated health data saved to {output_path}")
