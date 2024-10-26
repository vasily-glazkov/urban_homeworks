import os

import pandas as pd
from dotenv import load_dotenv
import requests
from matplotlib import pyplot as plt

load_dotenv()
API_KEY = os.getenv('API_KEY')


def display_weather_data(city: str):
    """
    Получает и отображает данные о прогнозе погоды на 5 дней для указанного города.

    Функция отправляет запрос к API OpenWeather для получения прогноза погоды
    на 5 дней с интервалом в 3 часа и отображает данные в виде графика температуры.
    Также вычисляет и выводит средние значения температуры и давления.

    Аргументы:
        city (str): Название города, для которого необходимо получить прогноз погоды.

    Действия:
        - Выполняет HTTP-запрос для получения данных о погоде.
        - Извлекает температуру и давление из ответа и сохраняет их в DataFrame.
        - Рассчитывает средние значения температуры и давления и выводит их в консоль.
        - Строит график изменения температуры по времени и отображает его с помощью matplotlib.

    Пример использования:
        display_weather_data('Murmansk')
    """
    # Запрашиваем данные о погоде с помощью библиотеки requests
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={API_KEY}'
    response = requests.get(url)
    data = None

    if response.status_code == 200:
        data = response.json()
    else:
        print("Ошибка получения данных - {response.status_code}")

    forecast_list = data['list']

    # Обрабатываем данные с помощью pandas
    # Извлекаем прогноз погоды и создаём DataFrame
    df = pd.DataFrame(forecast_list)

    # Разделим колонку 'main' для получения температуры и давления
    df['temperature'] = df['main'].apply(lambda x: x['temp'])
    df['pressure'] = df['main'].apply(lambda x: x['pressure'])
    df['date'] = pd.to_datetime(df['dt'], unit='s')

    # Выведем среднюю температуру и давление
    print("Средняя температура за период:", df['temperature'].mean())
    print("Среднее давление за период:", df['pressure'].mean())

    # Визуализация данных с помощью matplotlib
    # Построим график температуры на каждый день
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['temperature'], label='Температура (°C)', color='orange')
    plt.xlabel('Дата')
    plt.ylabel('Температура (°C)')
    plt.title(f'Прогноз погоды на 5 дней для города {city}')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    display_weather_data('Murmansk')
