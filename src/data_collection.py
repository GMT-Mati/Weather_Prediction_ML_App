import requests
import os

# Prompt the user for the API URL
API_URL = input("Enter the API URL (e.g., https://api.windy.com/api/point-forecast/v2): ")

# Prompt the user for the start date and end date
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Specify the location coordinates (latitude and longitude)
location = {"lat": 51.109, "lon": 15.381}

# Define the parameters for the API request
params = {
    "lat": location["lat"],
    "lon": location["lon"],
    "start": start_date,
    "end": end_date,
}

# Send a GET request to the Windy API
response = requests.get(API_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Save the response data as an HTML file
    output_dir = "data/html_output"
    os.makedirs(output_dir, exist_ok=True)
    output_filename = os.path.join(output_dir, f"weather_data_{start_date}_{end_date}.html")

    with open(output_filename, "w") as file:
        file.write(response.text)

    print(f"Data successfully collected and saved to {output_filename}")
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")
