# ************************************************
#
# Author: Стурейко Игорь
# Project: Geekbrains.WebDataParsing
# Lesson 2 - BeautifulSoup
# Date: 2020-04-11
#
# Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы)
# с сайта superjob.ru и hh.ru.
# Приложение должно анализировать несколько страниц сайта(также вводим через input или аргументы).
# Получившийся список должен содержать в себе минимум:
# *Наименование вакансии
# *Предлагаемую зарплату (отдельно мин. отдельно макс. и отдельно валюту)
# *Ссылку на саму вакансию
# *Сайт откуда собрана вакансия
# По своему желанию можно добавить еще работодателя и расположение.
# Данная структура должна быть одинаковая для вакансий с обоих сайтов.
# Общий результат можно вывести с помощью dataFrame через pandas.
#
# ************************************************

import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import json


def page_count(url: str, headers: {str: str}, params: {str: str}) -> int:
    res = requests.get(url, headers=headers, params=params)

    if res.ok:
        soup = bs(res.text, 'lxml')

        # разбираем - количество страниц в выдаче
        pages_group = soup.find_all('div', {'data-qa': 'pager-block'})[0]
        # получаем из словаря page_count
        # если page_count < 4 - то у нас в выдаче именно столько страниц
        # если 4 <= page_count < 6 - то разбираем span class='pager-item-not-in-short-range' и получаем 4 или 5 страниц
        # если page_count > 6 - то разбираем span за разделителем - оттуда выдергиваем конечное число страниц

        page_count = json.loads(pages_group.find_all('script')[0]['data-params'])['pagesCount']

        if page_count < 4:
            pass
        elif 4 <= page_count < 6:
            page_count = int(pages_group.find_all('span', {'class': 'pager-item-not-in-short-range'})[-1].getText())
        else:
            page_count = int(pages_group.find_all('span', {'class': 'pager-item-not-in-short-range'})[-1].find_all('a',
                                                                                                                   {
                                                                                                                       'class': 'bloko-button HH-Pager-Control'})[
                                 0].getText())

        return page_count
    else:
        return 0


if __name__ == '__main__':
    main_link = 'https://hh.ru/search/vacancy'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko)'\
        'Chrome/80.0.3987.163 Safari/537.36'}

    params = {'clusters': 'true',
              'area': '1',
              'enable_snippets': 'true',
              'salary': '',
              'st': 'searchVacancy',
              'text': 'Пекарь',
              'page': '0'
              }

    params1 = {'clusters': 'true',
               'area': '1',
               'enable_snippets': 'true',
               'salary': '',
               'st': 'searchVacancy',
               'text': 'Токарь',
               'page': '0'
               }

    params2 = {'clusters': 'true',
               'area': '1',
               'enable_snippets': 'true',
               'salary': '',
               'st': 'searchVacancy',
               'text': 'Python',
               'page': '0'
               }

    res = page_count(main_link, headers, params)
    print(f'\nПекарь: pages - {res}')

    res = page_count(main_link, headers, params1)
    print(f'\nТокарь: pages - {res}')

    res = page_count(main_link, headers, params2)
    print(f'\nPython: pages - {res}')
