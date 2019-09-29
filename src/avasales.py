import requests
import json
import re


def price_search(city_from, city_to):
    link = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20"+city_from+"%20в%20"+city_to
    resp = requests.get(link)
    data = json.loads(resp.text)
    return data


if (__name__) == '__main__':
    data = price_search("Москва", "Санкт-Петербург")
    print(data['origin']['iata'])
    print(data['destination']['iata'])

