# Integrated Helsinki Weather, Energy, and Health Data Analysis (April 2025)

This project demonstrates a full-stack data engineering pipeline that integrates **real hourly weather data, electricity consumption data, and simulated health emergency data** for Helsinki in April 2025. The workflow covers automated data fetching, cleaning, database integration, cross-domain merging, and multi-faceted exploratory analysis in Jupyter Notebooks.

---

## 📁 Project Structure

- `data/`: Source CSV files for weather, energy, and health data
- `notebooks/`: Jupyter notebooks with weather, energy, health, and combined analysis
- `scripts/`: Python scripts for fetching, simulating, and importing data
- `README.md`: Project documentation
- `requirements.txt`: Python dependencies
- `db_schema.sql`: SQL for creating PostgreSQL tables

---

## 📚 Data Domains and Sources

- **Weather:** Real data for Helsinki, April 2025 ([Visual Crossing API](https://www.visualcrossing.com/weather-api))
- **Energy Consumption:** Real hourly electricity data (Fingrid API or official CSV download)
- **Health (Emergency Visits):** Simulated hourly counts, matching the weather/energy time frame, designed to mimic real city hospital patterns

---

## 🌦️ Weather Data Acquisition

Weather data for Helsinki (April 2025) was obtained using the [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api):

```python
url = (
    f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    f"{location}/{start_date}/{end_date}"
    f"?unitGroup={unit_group}&include={include}&key={api_key}&contentType={content_type}"
)

    location: "Helsinki"
    start_date: "2025-04-01"
    end_date: "2025-05-01"
    unit_group: "metric"
    include: "hours"
    api_key: your Visual Crossing API key
    content_type: "csv" or "json"

📊 Key Features
Automated ETL pipeline: Fetches, cleans, and loads all data domains into PostgreSQL
Reproducible analyses: Individual notebooks for each domain, plus integrated analysis notebook
Advanced visualizations: Time series, correlation matrices, scatterplots, and event analysis across domains
Cross-domain integration: Joins data by timestamp for holistic insight
Lag and normalization features: Supports advanced analysis (e.g., lagged effects, rolling averages)
Portfolio-ready documentation: Clear code, comments, and project structure

🚀 How to Run

1. Clone this repository:
git clone https://github.com/yourusername/integrated-env-energy-health-pipeline.git
cd integrated-env-energy-health-pipeline

2. Set up PostgreSQL and create tables using db_schema.sql.
(Scripts are provided to import data to the database.)

3. Run scripts in /scripts to fetch/process weather, energy, and simulate health data.

4. Launch Jupyter Notebook:
    jupyter notebook

