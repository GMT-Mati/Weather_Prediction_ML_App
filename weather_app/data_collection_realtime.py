# weather_app/data_collection_realtime.py

import os
import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from django.conf import settings
from weather_app.models import WeatherData  # Import your WeatherData model

class Command(BaseCommand):
    help = 'Fetch and update real-time weather data'

    def handle(self, *args, **kwargs):
        api_key = 'YOUR_WINDY_API_KEY'  # Replace with your Windy API key
        api_url = 'https://api.windy.com/weather'  # Replace with the actual Windy API URL

        # Customize the API parameters (e.g., latitude, longitude, units) as needed
        params = {
            'lat': 51.109,
            'lon': 15.381,
            'units': 'metric',
            'key': api_key,
        }

        # Fetch real-time weather data from the Windy API
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            data = response.json()

            # Extract relevant data fields (customize based on API response structure)
            temperature = data['temperature']
            humidity = data['humidity']
            wind_speed = data['wind_speed']
            wind_direction = data['wind_direction']

            # Create a new WeatherData instance and save it to the database
            WeatherData.objects.create(
                date=datetime.now(),
                location='Real-Time Data Location',  # Customize as needed
                temperature=temperature,
                humidity=humidity,
                wind_speed=wind_speed,
                wind_direction=wind_direction,
            )

            self.stdout.write(self.style.SUCCESS('Successfully updated real-time weather data'))

        else:
            self.stdout.write(self.style.ERROR(f'Failed to fetch real-time weather data. Status code: {response.status_code}'))
