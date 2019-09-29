# 1. Напишите функцию получения IATA-кода города из его названия,
# используя API Aviasales для усовершенствования приложения по парсингу информации об авиабилетах,
# созданного нами в ходе урока.
#
# Примечание: воспользуйтесь документацией по API,
# которая доступна на странице www.aviasales.ru/API (ссылка на значке «API-документация»).
# Вам необходимо изучить раздел «API для определения IATA-кода».

import requests
import json
import re


def iata_search(city_name):
    """
    Поиск iata кодов по названию города
    :param city_name: название или часть названия города
    :return: список городов,
    :return: содержит ['country_name'], ['name'], ['code']
    """
    link = "http://autocomplete.travelpayouts.com/places2?term="+city_name+"&locale=en&types[]=city&callback=function"
    resp = requests.get(link)  # результат запроса
    data = json.loads(re.findall('function\((.*)\)\;', resp.text)[0])  # преобразуем в json
    try:  # проверяем на наличие ошибок
        if data['error']:
            print('Ошибка поиска, строка не содержит данных для поиска.')
            data = []
    except TypeError:
        pass

    return data


if (__name__) == '__main__':
    while True:
        f_str = input('Введите название города или его часть. Для выхода введите \'exit\': ')
        if f_str == 'exit':
            break
        else:
            data = iata_search(f_str)
            if len(data) > 0:
                for n in data:
                    print(n['country_name'] + ', ' + n['name'] + ': ' + n['code'])

