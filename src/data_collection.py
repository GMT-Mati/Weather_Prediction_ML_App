import requests
import os

# Define the API endpoint for historical weather data
API_URL = "https://www.windy.com/?51.109,15.381,8"
API_KEY = "uj83H5rjedSM7c6pZZYLCsYvEduKpbeh"  # Replace with your actual API key

# Specify the location coordinates (latitude and longitude) and the desired date range
location = {"lat": 51.109, "lon": 15.381}
start_date = "2023-09-06"
end_date = "2023-09-06"

# Define the parameters for the API request
params = {
    "key": API_KEY,
    "lat": location["lat"],
    "lon": location["lon"],
    "start": start_date,
    "end": end_date,
}

# Send a GET request to the Windy API
response = requests.get(API_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Create the path for storing the raw data file
    output_dir = "data/raw_data"
    os.makedirs(output_dir, exist_ok=True)
    output_filename = os.path.join(output_dir, f"weather_data_{start_date}_{end_date}.json")

    # Save the raw data to a JSON file
    with open(output_filename, "w") as file:
        file.write(response.text)

    print(f"Data successfully collected and saved to {output_filename}")
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")
