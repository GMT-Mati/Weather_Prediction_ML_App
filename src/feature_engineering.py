import os
import pandas as pd

# Define the path to the processed data file
processed_data_dir = "../data/processed_data"  # Adjust the path as needed
processed_data_file = "processed_weather_data.csv"  # Replace with the actual filename

# Define the path for storing the engineered features
engineered_features_dir = "../data/engineered_features"  # Adjust the path as needed
os.makedirs(engineered_features_dir, exist_ok=True)
engineered_features_file = os.path.join(engineered_features_dir, "engineered_features.csv")

# Load the processed data from the CSV file
processed_data_file_path = os.path.join(processed_data_dir, processed_data_file)
processed_df = pd.read_csv(processed_data_file_path)

# Perform feature engineering here
# Example: Create new features, aggregate data, calculate statistics, etc.
# Modify the code below to suit your specific feature engineering needs.

# Example: Calculate daily maximum temperature
daily_max_temperature = processed_df.groupby(processed_df["timestamps"].dt.date)["temperature"].max()
daily_max_temperature = daily_max_temperature.reset_index()
daily_max_temperature.columns = ["date", "max_temperature"]

# Save the engineered features as a CSV file
engineered_features.to_csv(engineered_features_file, index=False)

print(f"Engineered features saved to {engineered_features_file}")
