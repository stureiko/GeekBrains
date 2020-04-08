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
    url = 'https://api.github.com/users/' + user + '/repos'
    response = requests.get(url)

    if response.ok:
        data = json.loads(response.text)
        print(f'Для ползователя {user} найдены следующие репозитории:')
        for num in range(len(data)):
            print(f'\"{data[num]["name"]}\", language: {data[num]["language"]}')


# ************************************************
# Task 2
# ************************************************



def Task_2():
    site = 'https://api.vk.com/method/users.get'
    params = {'user_ids': '144051544',
              'fields': 'bdate',
              'access_token':'6a9c264b6e037ea6c66cc141b40ca13c87bf52cf2f7d9496d89a2b83b03f6687f73f672774572379a6522',
              'v': '5.103'
              }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    response = requests.get(site, headers=headers, params=params)
    print(response)
    data = json.loads(response.text)
    pprint(data)


if __name__ == '__main__':
    # Task_1()
    Task_2()