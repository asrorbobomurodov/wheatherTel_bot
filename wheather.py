import requests
from settings import API_KEY, TOKEN


def locat():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    res = requests.get(url)
    return res.json()['result'][-1]['message']['location']

def wheather(lat: int, long: int):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    header = {
        'X-RapidAPI-Key': '7b6fda4764msh668c091d72a8955p1a22e0jsn589019f17dfc',
        'X-RapidAPI-Host': 'yahoo-weather5.p.rapidapi.com'
    }

    params = {
        'lat': lat,
        'long': long
    }
    response = requests.get(url, params=params, headers=header)

    return response.json()

# print(wheather(lat=39.679931, long=66.980408))