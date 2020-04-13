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
import json
import re


# ************************************************
# Блок hh.ru
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


def decoder(mon)->[]:
    res = [None, None, None]
    if mon is not None:
        pos = re.findall(r'^\w+', mon)
        cur = re.findall(r'\b\S+[.]$', mon)
        if len(cur) > 0:
            res[2] = cur[0]
        strings = re.findall(r'\d+\s\d+', mon)
        if len(strings) > 1:
            for s in strings:
                r = ''
                for n in s.split('\xa0'):
                    r = r + n
                res[strings.index(s)] = int(r)
        elif len(strings) == 1:
            r = ''
            for n in strings[0].split('\xa0'):
                r = r + n
            if pos[0] == 'от':
                res[0] = int(r)
            else:
                res[1] = int(r)
    return res


def vacansies(vacans: bs4.element.Tag, vac_b: [])->[]:
    for vacancy in vacans.find_all('div', {'data-qa': 'vacancy-serp__vacancy'}):
        vac = {}
        vac['vacancy_name'] = vacancy.find_all('a', {'class': 'bloko-link'})[0].getText()
        vac['link'] = vacancy.find_all('a', {'class': 'bloko-link'})[0]['href']
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
        vac['vacancy_money'] = decoder(vacancy_money)
        vac['resource'] = 'hh.ru'
        vac_b.append(vac)
    return vac_b


def add_vac_in_base(res, base):
    if res.ok:
        soup = bs(res.text, 'lxml')
        base.append(vacansies(soup.find_all('div', {'class': 'vacancy-serp'})[0], base))

    del base[-1]
    return base


def get_hh(vac_name: str):
    main_link = 'https://hh.ru/search/vacancy'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko)'\
                      'Chrome/80.0.3987.163 Safari/537.36'}

    params = {'clusters': 'true',
               'area': '1',
               'enable_snippets': 'true',
               'salary': '',
               'st': 'searchVacancy',
               'text': vac_name,
               'page': '0'
               }

    vac_base = []
    par = params

    res = requests.get(main_link, headers=headers, params=par)
    if res.ok:
        soup = bs(res.text, 'lxml')
        pages = page_count(soup)
        print(f'HH page: 0 from {int(pages)}')
        vac_base.append(vacansies(soup.find_all('div', {'class': 'vacancy-serp'})[0], vac_base))
        del vac_base[-1]

    for n in range(1, pages):
        par['page'] = n
        res = requests.get(main_link, headers=headers, params=par)
        print(f'HH page: {par["page"]} from {int(pages)}')
        add_vac_in_base(res, vac_base)

    print(f'Обработано на HH.ru: {len(vac_base)} вакансий')

    return vac_base
# ************************************************


def ntraslit(w: str)->str:
    res = ''
    trans = {'а': 'a',
             'б': 'b',
             'в': 'v',
             'г': 'g',
             'д': 'd',
             'е': 'e',
             'ж': 'zh',
             'з': 'z',
             'и': 'i',
             'к': 'k',
             'л': 'l',
             'м': 'm',
             'н': 'n',
             'о': 'o',
             'п': 'p',
             'р': 'r',
             'с': 'c',
             'т': 't',
             'у': 'u',
             'ф': 'f',
             'х': 'h',
             'ц': 'c',
             'ч': 'ch',
             'ш': 'sh',
             'щ': 'sh',
             'ь': '',
             'ъ': '',
             'э': 'e',
             'ю': 'yu',
             'я': 'ya'}

    rus = re.match(r'^[а-я,А-Я]', w)
    if rus is not None:
        for l in w:
            res = res + trans[l]
        return res
    else:
        return w


# Блок superjob

def add_vac_sj_in_base(item: bs4.element.Tag, base):
    vac = {}
    vac_text = item.find('div', {'class': 'acdxh GPKTZ _1tH7S'}).find('a').getText()
    vac['vacancy_name'] = vac_text

    link = item.find('div', {'class': 'acdxh GPKTZ _1tH7S'}).find('a')['href']
    vac['link'] = link

    vac_company_block = item.find('span', {
        'class': '_3mfro _3Fsn4 f-test-text-vacancy-item-company-name _9fXTd _2JVkc _2VHxz _15msI'})
    if vac_company_block is not None:
        vac['vacancy_company'] = vac_company_block.find('a').getText()
    else:
        vac['vacancy_company'] = ''

    vac_adress_block = item.find('span',
                                 {'class': '_3mfro f-test-text-company-item-location _9fXTd _2JVkc _2VHxz'}).find(
        'span', {'class': 'clLH5'})
    if vac_adress_block is not None:
        vac['vacancy_address'] = vac_adress_block.find_next_sibling().getText()
    else:
        vac['vacancy_address'] = ''

    vac_describe_block = item.find('span', {'class': '_3mfro _3V-Qt _9fXTd _2JVkc _2VHxz'})
    if vac_describe_block is not None:
        vac['vacancy_describe_text'] = vac_describe_block.getText()
    else:
        vac['vacancy_describe_text'] = ''

    vac_price = item.find('div', {'class': 'acdxh GPKTZ _1tH7S'}).find('span', {
        'class': '_3mfro _2Wp8I _31tpt f-test-text-company-item-salary PlM3e _2JVkc _2VHxz'}).getText()
    vac['vacancy_money'] = decoder(vac_price)

    vac['resource'] = 'superjob.ru'

    base.append(vac)


def get_sj(vac_name: str):

    main_link = 'https://russia.superjob.ru/vacancy/search/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko)' \
                      'Chrome/80.0.3987.163 Safari/537.36'}

    params = {'keywords': vac_name.lower()}

    res = requests.get(main_link, headers=headers, params=params)
    vac_base = []
    page = 0

    if res.ok:
        soup = bs(res.text, 'lxml')

        vac_pages = soup.find_all('span', {'class': 'qTHqo _1mEoj _2h9me DYJ1Y _2FQ5q _2GT-y'})
        page = vac_pages[-2].getText()
        print(f'Sj page: 0 from {int(page)}')


        vac_bloc = soup.find_all('div', {'style': 'display:block'})[0]
        vacancy_items = vac_bloc.find_all('div', {'class': 'iJCa5 _2gFpt _1znz6 _2nteL'})

        for item in vacancy_items:
            add_vac_sj_in_base(item, vac_base)
    else:
        print(res)
        print(main_link)

    if int(page) > 0:
        for p in range(1, int(page)):
            params['page'] = str(p)
            res = requests.get(main_link, headers=headers, params=params)

            if res.ok:
                print(f'Sj page: {p} from {int(page)}')
                soup = bs(res.text, 'lxml')

                vac_bloc = soup.find_all('div', {'style': 'display:block'})[0]
                vacancy_items = vac_bloc.find_all('div', {'class': 'iJCa5 _2gFpt _1znz6 _2nteL'})

                for item in vacancy_items:
                    add_vac_sj_in_base(item, vac_base)
                # print(f'Добавлено васансий: {len(vac_base)}')
            else:
                print(res)
                print(main_link)

    print(f'Обработано на Sj.ru: {len(vac_base)} вакансий')
    return vac_base
# ************************************************


if __name__ == '__main__':
    vac_name = 'python'

    file_name = 'vacancies_' + ntraslit(vac_name) + '.json'

    vac_base = get_hh(vac_name) + get_sj(vac_name)

    with open(file_name, "w") as write_file:
        json.dump(vac_base, write_file)


