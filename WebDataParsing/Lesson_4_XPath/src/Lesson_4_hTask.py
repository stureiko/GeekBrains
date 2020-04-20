# ************************************************
#
# Author: Стурейко Игорь
# Project: Geekbrains.WebDataParsing
# Lesson 4 - XPath
# Date: 2020-04-18
#
# 1)Написать приложение, которое собирает основные новости с сайтов mail.ru, lenta.ru, yandex-новости.
#
# Для парсинга использовать xpath. Структура данных должна содержать:
# •	название источника,
# •	наименование новости,
# •	ссылку на новость,
# •	дата публикации
#
# ************************************************

import requests
from lxml import html
from pymongo import MongoClient


def get_yandex_news()->[]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko)' \
                      'Chrome/80.0.3987.163 Safari/537.36'}

    main_link = 'https://yandex.ru/news/'

    source_string = main_link

    response = requests.get(source_string, headers=headers)
    print("Yandex news: " + str(response))

    root = html.fromstring(response.text)
    items = root.xpath("//td[@class='stories-set__item']")
    result = []
    for item in items:
        dict = {}
        dict['title'] = item.xpath("./div/div[@class='story__topic']/h2/a/text()")[0]
        dict['link'] = "https://yandex.ru" + item.xpath("./div/div[@class='story__topic']/h2/a/@href")[0]
        line = item.xpath("./div/div[@class='story__info']/div[@class='story__date']/text()")[0]

        news_date = line[-5:]
        news_source = line[:-5]
        dict['date'] = news_date
        dict['source'] = news_source
        result.append(dict)

    return result

def get_mail_news()->[]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko)' \
                      'Chrome/80.0.3987.163 Safari/537.36'}

    main_link = 'https://news.mail.ru'

    source_string = main_link

    response = requests.get(source_string, headers=headers)
    print("Mail.ru news: " + str(response))
    result = []

    root = html.fromstring(response.text)
    # блок главные новости
    items = root.xpath("//div[@class='js-module'][@data-module='TrackBlocks']")
    item = items[0]
    news = item.xpath("./ul/li/a")
    for news_item in news:
        dict = {}
        dict['title'] = news_item.xpath("./text()")[0]
        dict['link'] = main_link + news_item.xpath("./@href")[0]
        result.append(dict)
    # конец блока главные новости

    # блок новости региона
    items = root.xpath("//div[contains(@class, 'block block_bg_primary block_separated_top link-hdr')]/div/div/div[@class='cols__wrapper']")
    item = items[0]
    news = item.xpath("./div/div/ul/li/span")
    for news_item in news:
        dict = {}
        dict['title'] = news_item.xpath("./a/span/text()")[0]
        dict['link'] = main_link + news_item.xpath("./a/@href")[0]
        result.append(dict)
    # конец блока новости региона

    # Осоновной новостной блок
    items = root.xpath("//div[@class = 'block block_separated_top rb_nat']")
    item = items[0]
    news = item.xpath("./div/div/div/div/div/ul/li/span")
    for news_item in news:
        dict = {}
        dict['title'] = news_item.xpath("./a/span/text()")[0]
        dict['link'] = main_link + news_item.xpath("./a/@href")[0]
        result.append(dict)
    # Конец основного новостного блока

    return result

#TODO: получить новости с lenta.ru
#TODO: проверить разбор даты


if __name__ == '__main__':
    news = get_yandex_news() + get_mail_news()

    client = MongoClient('localhost', 27017)
    db = client['news']
    # выбор коллекции документов
    coll = db['news']

    print(coll.estimated_document_count())

    for n in news:
        coll.update_one({'link': n['link']}, {'$set': n}, upsert=True)

    print(coll.estimated_document_count())

