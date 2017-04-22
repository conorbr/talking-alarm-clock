# Weather Forecast Module

import json
from myql.contrib.weather import Weather

def get_weather(location="Dublin IRL"):

    # Query weather from Yahoo Weather using mYQL
    weather = Weather(unit='c', format='json')
    req_obj = json.loads(weather.get_weather_in(location).text)
    req_obj = req_obj['query']['results']['channel']

    # Create dictionary object to return
    ret_obj = {}
    try:
        ret_obj['temp'] = req_obj['item']['condition']['temp']
        ret_obj['high'] = req_obj['item']['forecast'][0]['high']
        ret_obj['low'] = req_obj['item']['forecast'][0]['low']
        ret_obj['condition'] = req_obj['item']['condition']['text']
        ret_obj['humidity'] = req_obj['atmosphere']['humidity']
        ret_obj['city'] = req_obj['location']['city']
    except KeyError:
        print("Failed to fetch weather conditions.")
        return False

    return ret_obj
