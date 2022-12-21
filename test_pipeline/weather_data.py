
import requests
from jsonparse import Parser

from gluetube.pipeline import stage


@stage(1, 'get weather')
def get_weather():
    return requests.get('https://wttr.in/Vancouver?format=j1').json()


@stage(2, 'write weather to file')
def write_out_avg_temps(data):
    with open('weather.json', 'x') as f:
        f.write(str(Parser().find_keys(data, ['date', 'avgtempC'])))


weather = get_weather()
write_out_avg_temps(weather)
