# weather_app/model_retraining.py

import os
import pandas as pd
from django.core.management.base import BaseCommand
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
from weather_app.models import WeatherData  # Import your WeatherData model

class Command(BaseCommand):
    help = 'Retrain the machine learning model with combined data and deploy it'

    def handle(self, *args, **kwargs):
	try:
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
	
	        # Define the directory to store the model
	        model_dir = "models"  # Replace with the path to your models directory
	        os.makedirs(model_dir, exist_ok=True)
	
	        # Define the model filename
	        model_filename = os.path.join(model_dir, "weather_prediction_model.pkl")
	
	        # Delete the existing model file (if it exists)
	        if os.path.exists(model_filename):
	            os.remove(model_filename)
	
	        # Save the trained model
	        joblib.dump(model, model_filename)
	
	        self.stdout.write(self.style.SUCCESS('Model retraining and update completed'))
	
	        # Perform model deployment here (e.g., restart the web server or update a model reference)
            # Log a success message
            self.stdout.write(self.style.SUCCESS('Model retraining and update completed'))

            # Perform model deployment here (e.g., restart the web server or update a model reference)

        except Exception as e:
            # Log an error message
            self.stderr.write(self.style.ERROR(f'Model retraining failed with error: {str(e)}'))

            # Trigger an alert (e.g., send an email or use a monitoring service API)
