import os
from pprint import pprint

import aiohttp
import asyncio
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')
city = 'Murmansk'
GEOCODE_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"


async def get_coordinates():
    async with aiohttp.ClientSession() as session:
        async with session.get(GEOCODE_URL) as response:
            if response.status == 200:
                data = await response.json()
                return data[0]['lat'], data[0]['lon']
            else:
                print(f"Ошибка: {response.status}")
                return None


lat, lon = asyncio.run(get_coordinates())

WEATHER_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"

response = requests.get(WEATHER_URL)

if response.status_code == 200:
    weather_data = response.json()
    print("Данные успешно получены")
else:
    print(f"Ошибка получения данных - {response.status_code}")

current_temp = weather_data['main']['temp']
current_wind = weather_data['wind']['speed']
sky_condition = weather_data['weather'][0]['main']
print(f"Текущая погода для города {city}\n"
      f"Температура: {current_temp}\n"
      f"Ветер {current_wind}\n"
      f"{sky_condition}")
