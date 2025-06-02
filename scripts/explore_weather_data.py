import pandas as pd

print("🔧 Script has started")

# Load the data
file_path = "../data/helsinki_weather_april_2025.csv"
df = pd.read_csv(file_path)

# Show the shape and first few rows
print(f"✅ Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns\n")
print(df.head())

# List all columns
print("\n📋 Columns:")
print(df.columns.tolist())

# Summary statistics
print("\n📊 Summary Statistics:")
print(df.describe(include='all'))

# Check for missing values
print("\n🔍 Missing values per column:")
print(df.isnull().sum())
