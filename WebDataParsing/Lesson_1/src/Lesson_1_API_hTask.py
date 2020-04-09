# ************************************************
#
# Author: Стурейко Игорь
# Project: Geekbrains.WebDataParsing
# Lesson 1 - API
# Date: 2020-04-08
#
# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев
# для конкретного пользователя, сохранить JSON-вывод в файле *.json.
#
# 2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
#
# ************************************************

# ************************************************
# Task 1
# ************************************************

import requests
import json
from pprint import pprint


def input_user_name()->str:
    welcome = 'Введите имя пользователя для поиска на Github: '
    s = input(welcome)

    while True:
        if s:
            print('\n')
            return s
        else:
            print('Вы не ввели имя пользователя, попробуйте еще раз')
            s = input(welcome)


def Task_1():
    print('*'*30)
    print(' '* 5 + 'Task 1')
    user = input_user_name()
    # user = 'stureiko'
    url = 'https://api.github.com/users/' + user + '/repos'
    params = {'per_page': '20',
              'page': '1'
              }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    response = requests.get(url, params=params, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        print(f'Для ползователя {user} найдены следующие репозитории:')

        while len(data) > 0:
            pprint(len(data))
            for num in range(len(data)):
                print(f'\"{data[num]["name"]}\", language: {data[num]["language"]}')
            i = int(params['page'])
            params['page'] = str(i+1)
            response = requests.get(url, params=params, headers=headers)
            data = json.loads(response.text)
    else:
        print(response)
        print(response.text)

# ************************************************
# Task 2
# ************************************************

def Task_2():
# Получение стоимости авиабилетов с aviasales
    site = 'http://api.travelpayouts.com/v2/prices/latest'
    params = {'currency': 'rub',
              'period_type': 'month',
              'origin': 'DME',
              'destination': 'BER',
              'beginning_of_period': '2020-08-01',
              'page': '1',
              'limit': '30',
              'show_to_affiliates': 'true',
              'sorting': 'price',
              'token': '2307a34ffd39b622193e2cdadc5e99d1'
              }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    response = requests.get(site, headers=headers, params=params)

    if response.ok:
        data = json.loads(response.text)

        with open('Task_2_aviasales_answer.json', 'w') as f:
            f.write(json.dumps(data))

        with open('Task_2_full_answer.txt', 'w') as f:
            f.write(str(response.headers))
            f.write(str(response.text))


if __name__ == '__main__':
    Task_1()
    # Task_2()
