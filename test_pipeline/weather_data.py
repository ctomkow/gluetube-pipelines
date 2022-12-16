
import requests
from jsonparse import Parser

from gluetube.pipeline import stage


@stage(1, 'get weather')
def get_weather():
    return requests.get('https://wttr.in/Vancouver?format=j1').json()


@stage(2, 'display weather')
def display_avg_temps(data):
    print(Parser().find_keys(data, ['date', 'avgtempC']))


weather = get_weather()
display_avg_temps(weather)
