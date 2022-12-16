
import requests
from jsonparse import Parser

data = requests.get('https://wttr.in/Vancouver').json()

# todo: work in progress
