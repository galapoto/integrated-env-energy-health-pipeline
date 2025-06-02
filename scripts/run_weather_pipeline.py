import os
import subprocess
from datetime import datetime

def run_step(script_name):
    print(f"\n🚀 Running: {script_name}")
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"❌ {script_name} failed with error:\n{result.stderr}")
        exit(1)

def main():
    print("🔁 Starting Weather Pipeline")

    # Step 1: Fetch latest weather data
    run_step("fetch_helsinki_weather.py")

    # Step 2: Store to PostgreSQL
    run_step("load_weather_to_db.py")

    print("✅ Pipeline completed at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()