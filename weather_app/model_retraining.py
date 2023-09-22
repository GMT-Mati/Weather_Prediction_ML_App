# weather_app/model_retraining.py

import os
import pandas as pd
from django.core.management.base import BaseCommand
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
from weather_app.models import WeatherData  # Import your WeatherData model

class Command(BaseCommand):
    help = 'Retrain the machine learning model with combined data'

    def handle(self, *args, **kwargs):
        # Load historical data from the database
        historical_data = WeatherData.objects.all().values()

        # Convert historical data to a DataFrame
        historical_df = pd.DataFrame.from_records(historical_data)

        # Fetch real-time data from the database (or another source)
        real_time_data = WeatherData.objects.filter(location='Real-Time Data Location').values()

        # Convert real-time data to a DataFrame
        real_time_df = pd.DataFrame.from_records(real_time_data)

        # Merge real-time data with historical data (concatenate DataFrames)
        combined_df = pd.concat([historical_df, real_time_df], ignore_index=True)

        # Preprocess and prepare the combined dataset for model training
        # You can apply any necessary feature engineering and data cleaning steps here

        # Split the data into features (X) and target (y)
        X = combined_df.drop(columns=['temperature'])  # Adjust columns as needed
        y = combined_df['temperature']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a machine learning model (Random Forest Regressor, for example)
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Evaluate the model's performance on the test set (optional)
        test_score = model.score(X_test, y_test)
        print(f'Model Test Score: {test_score}')

        # Save the trained model
        model_dir = "models"  # Replace with the path to your models directory
        os.makedirs(model_dir, exist_ok=True)
        model_filename = os.path.join(model_dir, "weather_prediction_model.pkl")
        joblib.dump(model, model_filename)

        self.stdout.write(self.style.SUCCESS('Model retraining and update completed'))
