import datetime as dt
from datetime import date
import requests
import art


print(art.logo)
searched_city = input("Please input city name: ")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = '
CITY = searched_city
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()


def kelvin_to_c_f(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit


today_date_time = date.today()
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_c_f(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_c_f(feels_like_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
country = response['sys']['country']

print(f"Date: {today_date_time}")
print('----')
print(f"Location: {CITY.title()}, {country} \nTemp: {temp_celsius:.1f}c, Feels like: {feels_like_celsius:.1f}c")
print(f"Humidity: {humidity}% \nSunrise: {sunrise_time}, \nSunset: {sunset_time}")

