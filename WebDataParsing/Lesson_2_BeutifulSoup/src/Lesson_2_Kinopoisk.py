# Lesson 2 - BeutifulSoup - Kinopoisk
# Получить список премьер
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

if __name__ == '__main__':
    main_link = 'https://www.kinopoisk.ru'

    # получить содержимое страницы с премьерами для разбора
    response = requests.get(f'{main_link}/premiere/').text

    # разбираем страницу
    soup = bs(response, 'lxml')

    # ищем div с классом "prem_list" - сам список премьер
    films_block = soup.find_all('div', {'class': 'prem_list'})[1]

    # извлекаем содержимое - div с фильмами
    films_list = films_block.find_all('div', {'class': 'premier_item'})

    # смотрим длину списка
    print(f'Всего {len(films_list)} фильмов.')

    # список словарей для хранения информации о фильмах
    films = []
    for film in films_list:
        film_data = {}

        # извлекаем из карточки фильма ссылку на его страницу и название
        name = film.find('div', {'class': 'text'}).find('span', {'class': 'name'}).find('a')

        # выделяем жанр
        genre = film.find('div', {'class': 'text'}).find('div', {'class': 'textBlock'}).find_all('span')[-2]. \
            getText().replace('(', '').replace(')', '').replace('...', '')

        # выделяем ссылку на страницу фильма
        link = name['href']

        # выделяем название фильма изаносим данные в словарь
        film_data['name'] = name.getText()
        film_data['link'] = main_link + name['href']
        film_data['genre'] = genre

        # добавляем данные в список с фильмами
        films.append(film_data)

    # распечатать результат
    for film in films:
        print(film)
