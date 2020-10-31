"""
    Файл для функций и классов работающих вне дискорда
"""
import logging
import socket
import random
import re

import requests
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from bs4 import BeautifulSoup as bs

from config import OWM_API_KEY


def weather(city_from_discord):
    """
    Принимает на вход название города и выводит прогноз погоды
    """
    config_dict = get_default_config()
    config_dict['language'] = 'ru'  # your language here
    owm = OWM(OWM_API_KEY, config_dict)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city_from_discord)
    weather = observation.weather
    temperature = weather.temperature('celsius')['temp']
    full_message = f'{weather.detailed_status.capitalize()}, температура в городе {city_from_discord} {round(temperature)}°C'
    return full_message


def make_bin_string(text_str):
    """
    Принимает на вход строку и выводит бинарный код
    """
    return ''.join(format(ord(i), 'b') for i in text_str)


class Joke_Parser:
    def __init__(self):
        self.num_page = random.randint(2, 109)
        self.num_joke = random.randint(1, 28)
        print(self.num_joke)
        print(self.num_page)

    def get_joke(self):
        """Парсит html и радномно выбирает шутку с него"""
        r = requests.get(f'https://4tob.ru/anekdots/page{self.num_page}')  # 2..109
        if r.status_code != 200:
            logging.warning(f'Failed to connection to server, response.status_code = {r.status_code}')
            return 'Failed'
        page_text = r.text
        soup = bs(page_text, 'html.parser')
        result = soup.find_all('div', 'text')
        print(result)
        for i in range(len(result)):
            result[i] = re.sub(r'<br/>', '\n', str(result[i]))
            result[i] = re.sub(r'<p>', '\n', result[i])
            result[i] = re.sub(r'</p>', '', result[i])
            result[i] = re.sub(r'<div class="text">', '', result[i])
            result[i] = re.sub(r'</div>', '', result[i])
        return result[self.num_joke]
