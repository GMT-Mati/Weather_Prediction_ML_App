import os
import pandas as pd

# Define the path to the raw data file
raw_data_dir = "../data/raw_data"  # Adjust the path as needed
raw_data_file = "weather_data_2023-01-01_2023-01-07.json"  # Replace with the actual filename

# Define the path for storing the processed data
processed_data_dir = "../data/processed_data"  # Adjust the path as needed
os.makedirs(processed_data_dir, exist_ok=True)
processed_data_file = os.path.join(processed_data_dir, "processed_weather_data.csv")

# Load the raw data from the JSON file
raw_data_file_path = os.path.join(raw_data_dir, raw_data_file)
raw_df = pd.read_json(raw_data_file_path)

# Perform data cleaning and preprocessing here
# Example: Drop unnecessary columns, handle missing values, convert data types, etc.
# Modify the code below to suit your specific data preprocessing needs.

# Drop unnecessary columns
raw_df.drop(["timezone", "current", "units"], axis=1, inplace=True)

# Convert timestamps to datetime objects
raw_df["timestamps"] = pd.to_datetime(raw_df["timestamps"], unit="s")

# Save the processed data as a CSV file
processed_df.to_csv(processed_data_file, index=False)

print(f"Processed data saved to {processed_data_file}")
