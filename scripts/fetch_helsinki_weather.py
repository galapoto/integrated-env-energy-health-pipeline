import requests

# Define parameters
location = "Helsinki"
start_date = "2025-04-01"
end_date = "2025-04-30"
unit_group = "metric"
include = "hours"
content_type = "csv"
api_key = "GV6SMHVC63ZWD9C56MK9AXCGV"  # Replace with your Visual Crossing API key

# Construct the API URL
url = (
    f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    f"{location}/{start_date}/{end_date}"
    f"?unitGroup={unit_group}&include={include}&key={api_key}&contentType={content_type}"
)

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    file_path = "../data/helsinki_weather_april_2025.csv"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(response.text)
    print(f"Data successfully saved to '{file_path}'")
else:
    print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
    print("Response:", response.text)