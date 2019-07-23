#creates a function API that retrieves the weather data 
# based on the city selected
from datetime import datetime
import os
import pytz
import requests
import math 

API_KEY = '205cad2e62ebd0a8d447e9d978a76ab5'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')

def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data

