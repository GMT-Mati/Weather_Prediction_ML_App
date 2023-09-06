import os
import pandas as pd
import jsonschema
import json

# Prompt the user for the filename in the data/raw_data folder
raw_data_folder = "data/raw_data"
files = os.listdir(raw_data_folder)
print("Available raw data files:")
for i, filename in enumerate(files):
    print(f"{i + 1}. {filename}")

try:
    choice = int(input("Enter the number of the file you want to process: "))
    selected_file = files[choice - 1]
except (ValueError, IndexError):
    print("Invalid choice. Please enter a valid number.")
    exit(1)

# Define the path to the selected raw data file
raw_data_file_path = os.path.join(raw_data_folder, selected_file)

# Load the JSON schema for validation (customize as needed)
json_schema = {
    "type": "object",
    "properties": {
        "timestamps": {"type": "array"},
        "temperature": {"type": "array"},
        "humidity": {"type": "array"},
        # Add more properties as needed
    },
    # Add more validation rules as needed
}

try:
    # Load the raw data from the JSON file
    with open(raw_data_file_path, "r") as json_file:
        data = json.load(json_file)

    # Validate the data against the JSON schema
    jsonschema.validate(data, json_schema)

    # Continue with data preprocessing
    raw_df = pd.DataFrame(data)

    # Perform data preprocessing here
    # Example: Drop unnecessary columns, handle missing values, convert data types, etc.
    # Modify the code below to suit your specific data preprocessing needs.

    # Drop unnecessary columns
    raw_df.drop(["timezone", "current", "units"], axis=1, inplace=True)

    # Convert timestamps to datetime objects
    raw_df["timestamps"] = pd.to_datetime(raw_df["timestamps"], unit="s")

    # Save the processed data as a CSV file
    processed_data_dir = "data/processed_data"
    os.makedirs(processed_data_dir, exist_ok=True)
    processed_data_file = os.path.join(processed_data_dir, f"processed_{selected_file}.csv")
    raw_df.to_csv(processed_data_file, index=False)

    print(f"Processed data saved to {processed_data_file}")

except jsonschema.ValidationError as e:
    print(f"JSON data validation error: {e}")
except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")

