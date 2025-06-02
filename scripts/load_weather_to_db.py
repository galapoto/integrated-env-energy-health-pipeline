import pandas as pd
from sqlalchemy import create_engine
import os

# Database config
DB_NAME = "weather_db"
DB_USER = "postgres"
DB_PASS = "Papajohn.1234" 
DB_HOST = "localhost"
DB_PORT = "5432"

# Load the CSV
file_path = "../data/helsinki_weather_april_2025.csv"
df = pd.read_csv(file_path)

# Convert datetime column to real datetime objects
df["datetime"] = pd.to_datetime(df["datetime"])

# Create database connection string
db_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

# Write data into the database table
df.to_sql("weather_data", engine, if_exists="append", index=False)

print("Data loaded into PostgreSQL table 'weather_data'")