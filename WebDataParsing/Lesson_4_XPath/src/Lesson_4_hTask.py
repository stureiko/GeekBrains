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
from pprint import pprint


def get_yandex_news()->[]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko)' \
                      'Chrome/80.0.3987.163 Safari/537.36'}

    main_link = 'https://yandex.ru/news/'

    source_string = main_link

    response = requests.get(source_string, headers=headers)
    print(response)

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
        # dict['date'] = item.xpath("./div/div[@class='story__info']/div[@class='story__date']/text()")[0]
        dict['date'] = news_date
        dict['source'] = news_source
        result.append(dict)

    return result


if __name__ == '__main__':
    pprint(get_yandex_news())
