# weather_app/data_preprocessing_realtime.py

import os
import pandas as pd
from django.core.management.base import BaseCommand
from weather_app.models import WeatherData  # Import your WeatherData model

class Command(BaseCommand):
    help = 'Preprocess and merge real-time weather data with historical data'

    def handle(self, *args, **kwargs):
        # Load historical data from the database
        historical_data = WeatherData.objects.all().values()

        # Convert historical data to a DataFrame
        historical_df = pd.DataFrame.from_records(historical_data)

        # Fetch real-time data from the database (or another source)
        real_time_data = WeatherData.objects.filter(location='Real-Time Data Location').values()

        # Convert real-time data to a DataFrame
        real_time_df = pd.DataFrame.from_records(real_time_data)

        # Preprocess real-time data (apply the same preprocessing steps as for historical data)
        # For example, you can convert date strings to datetime objects and handle missing values

        # Merge real-time data with historical data (concatenate DataFrames)
        merged_df = pd.concat([historical_df, real_time_df], ignore_index=True)

        # Save the merged data back to the database or as a CSV file, as needed
        # For example, you can use the `to_sql` method to save it to a database table

        self.stdout.write(self.style.SUCCESS('Successfully preprocessed and merged real-time weather data'))
