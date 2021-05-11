# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:59:11 2021

@author: Dipen
"""
import requests
from pprint import pprint #pretty print for json


Api_key = 'fad1327dac8dd23f6112443ae07c5499'

city = input('Enter a city: ')

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+Api_key+"&q="+city
print(base_url)

weather_data = requests.get(base_url).json()

pprint(weather_data)
