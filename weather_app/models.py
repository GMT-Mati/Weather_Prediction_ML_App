from django.db import models

class WeatherData(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.CharField(max_length=20)
    # Add more fields as needed for your weather data

    def __str__(self):
        return f"{self.date} - {self.location}"
