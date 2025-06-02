import pandas as pd
from sqlalchemy import create_engine, Table, Column, Float, Integer, String, MetaData, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
import os

# Database config
DB_NAME = "weather_db"
DB_USER = "postgres"
DB_PASS = "Papajohn.1234"      
DB_HOST = "localhost"
DB_PORT = "5432"

# Load the CSV to detect columns and types
file_path = "../data/helsinki_weather_april_2025.csv"
df = pd.read_csv(file_path)

# Convert datetime
df["datetime"] = pd.to_datetime(df["datetime"])

# Create connection string
db_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)
conn = engine.connect()
metadata = MetaData()

# Define SQL table schema
weather_table = Table("weather_data", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("datetime", DateTime),
    Column("temp", Float),
    Column("feelslike", Float),
    Column("dew", Float),
    Column("humidity", Float),
    Column("precip", Float),
    Column("precipprob", Float),
    Column("preciptype", String),
    Column("snow", Float),
    Column("snowdepth", Float),
    Column("windgust", Float),
    Column("windspeed", Float),
    Column("winddir", Float),
    Column("sealevelpressure", Float),
    Column("cloudcover", Float),
    Column("visibility", Float),
    Column("solarradiation", Float),
    Column("solarenergy", Float),
    Column("uvindex", Float),
    Column("severerisk", String),
    Column("conditions", String),
    Column("icon", String),
    Column("stations", String),
)

# Create the table
metadata.drop_all(engine, tables=[weather_table])  # drops if exists
metadata.create_all(engine)
print("✅ Table 'weather_data' created successfully.")