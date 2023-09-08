import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor  # Replace with the model of your choice
import joblib

# Define file paths for the engineered features and the model
engineered_features_path = "../data/engineered_features/engineered_features.csv"  # Adjust the path as needed
model_save_path = "../models/trained_model.pkl"  # Adjust the path and file format based on your model choice

# Load the engineered features
engineered_features_df = pd.read_csv(engineered_features_path)

# Prepare the feature matrix (X) and target variable (y)
X = engineered_features_df.drop(columns=["max_temperature"])  # Adjust the target variable column name
y = engineered_features_df["max_temperature"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the machine learning model (replace with the model of your choice)
model = RandomForestRegressor(n_estimators=100, random_state=42)  # Example: Random Forest Regressor
model.fit(X_train, y_train)

# Evaluate the model (you can add model evaluation code here)

# Save the trained model to the models folder
os.makedirs("../models", exist_ok=True)
joblib.dump(model, model_save_path)

print(f"Trained model saved to {model_save_path}")
