import requests
from pprint import pprint

API_KEY = "cb771e45ac79a4e8e2205c0ce66ff633"

city = input("Enter a City : ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid=" + API_KEY + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)