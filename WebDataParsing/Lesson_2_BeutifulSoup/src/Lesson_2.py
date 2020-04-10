# Lesson 2 - BeutifulSoup
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint


def response(url: str)->str:
    res = requests.get(url)
    res.encoding = 'utf-8'
    if res.ok:
        return res.text
    else:
        return str(res)

#
# def parse(text: str)->str:
#     soup = bs(text, 'lxml')
#     res = soup.find_all('a')
#     print(type(res))
#     return res


if __name__ == '__main__':
    text = response('http://localhost/Fitness')
    soup = bs(text, 'lxml')

    # Плиск по цепочке элементов
    # pprint(soup.find_all('div')[0])
    # res = soup.find_all('div')[0].find_all('li')
    # # print(len(res))
    # print('*'*30)
    # pprint(res)

    # Поиск по атрибуту (class="shopUnitName")
    # res = soup.find_all(attrs={'class': 'shopUnitName'})
    # pprint(res)

     # Поиск по конкретному тегу
    # res = soup.find_all('div', {'class': 'shopUnitName'})
    # pprint(res)

    # Поиск только какого-то числа первых вхождений
    # res = soup.find_all('div', limit=3)
    # pprint(len(res))

    # Поиск по содержимому
    # ДОЛЖНО ПОЛНОСТЬЮ СОВПАДАТЬ С ТЕКСТОМ ЭЛЕМЕНТА
    # res = soup.find_all(text='Название продукта')
    # pprint(res)
