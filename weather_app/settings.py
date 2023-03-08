from os import environ

SECRET_KEY = environ.get('SECRET_KEY')
WEATHER_API = environ.get('WEATHER_API')
WEATHER_BASE_URL = environ.get('WEATHER_BASE_URL')
