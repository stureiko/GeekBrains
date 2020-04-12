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
import bs4
from bs4 import BeautifulSoup as bs
from pprint import pprint
import json


def page_count(soup: bs) -> int:
    # разбираем - количество страниц в выдаче
    pages_group = soup.find_all('div', {'data-qa': 'pager-block'})[0]
    # получаем из словаря page_count
    # если page_count < 4 - то у нас в выдаче именно столько страниц
    # если 4 <= page_count < 6 - то разбираем span class='pager-item-not-in-short-range' и получаем 4 или 5 страниц
    # если page_count > 6 - то разбираем span за разделителем - оттуда выдергиваем конечное число страниц

    page_count = json.loads(pages_group.find_all('script')[0]['data-params'])['pagesCount']

    if page_count < 4:
        return page_count
    elif 4 <= page_count < 6:
        return int(pages_group.find_all('span', {'class': 'pager-item-not-in-short-range'})[-1].getText())
    else:
        return int(pages_group.find_all('span', {'class': 'pager-item-not-in-short-range'})[-1].\
                   find_all('a', {'class': 'bloko-button HH-Pager-Control'})[0].getText())

def vacansies(vacans: bs4.element.Tag, vac_b: [])->[]:
    for vacancy in vacans.find_all('div', {'data-qa': 'vacancy-serp__vacancy'}):
        vac = {}
        vac['vacancy_name'] = vacancy.find_all('a', {'class': 'bloko-link'})[0].getText()
        vac['vacancy_company'] = vacancy.find_all('div', {'class': 'vacancy-serp-item__meta-info'})[0].find_all('a', {'class': 'bloko-link'})[0].getText()
        vac['vacancy_address'] = vacancy.find_all('span', {'data-qa': 'vacancy-serp__vacancy-address'})[0].getText()
        vacancy_describe = vacancy.find_all('div', {'class': 'g-user-content'})[0].find_all('div')
        vacancy_describe_text = ''
        for s in vacancy_describe:
            vacancy_describe_text = vacancy_describe_text + s.getText()
        vac['vacancy_describe_text'] = vacancy_describe_text

        vacancy_money = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})

        if vacancy_money != None:
            vacancy_money = vacancy_money.getText()
        vac['vacancy_money'] = vacancy_money

        vac_b.append(vac)
    return vac_b


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

    vac_base = []
    par = params1

    res = requests.get(main_link, headers=headers, params=par)
    print(f'Current page: {par["page"]}')
    if res.ok:
        soup = bs(res.text, 'lxml')
        pages = page_count(soup)
        vac_base.append(vacansies(soup.find_all('div', {'class': 'vacancy-serp'})[0], vac_base))
        del vac_base[-1]

    for n in range(1, pages):
        par['page'] = n
        res = requests.get(main_link, headers=headers, params=par)
        print(f'Current page: {par["page"]}')
        if res.ok:
            soup = bs(res.text, 'lxml')
            pages = page_count(soup)
            vac_base.append(vacansies(soup.find_all('div', {'class': 'vacancy-serp'})[0], vac_base))
            del vac_base[-1]

    for vac in vac_base:
        print(vac)
        print('* '*20)

    print(f'Обработано: {len(vac_base)} вакансий')
