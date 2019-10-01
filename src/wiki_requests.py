import collections
import re
from requests import get
from bs4 import BeautifulSoup as BS


def get_link(topic: str):
    """
    Получает в корректном виде топик для формирвоания ссылки на страницу wiki
    :param topic:
    :return: строка содержащая корректную ссылку на страницу wiki
    """
    link = "https://ru.wikipedia.org/wiki/" + topic.capitalize()
    return link


def get_topic_page(topic: str):
    """
    Получает html код страницы wiki
    :param topic:
    :return: строка html кода
    """
    link = get_link(topic)
    html_content = get(link).text
    return html_content


def get_topic_words(topic: str):
    """
    Получает русский текст со страницы wiki в виде набора слов
    :param topic:
    :return: список слов
    """
    html_content = get_topic_page(topic)
    words = re.findall('[а-яА-Я\-\']{3,}', html_content)
    return words


def get_topic_text(topic: str):
    """
    Получает русский текст со страницы wiki
    :param topic:
    :return: строка содержащая текст со страницы wiki
    """
    text = ' '.join(get_topic_words(topic))
    return text


def get_common_words(topic: str):
    """
    Полчает список кортежей (слово, частота в тексте) отсортировано по убыванию частоты
    :param topic:
    :return:
    """
    words = get_topic_words(topic)
    rate = collections.Counter(words).most_common()
    return rate


def get_page_links(topic: str):
    """
    Получение всех ссылок со страницы, которые указывают на страницы wiki
    :param topic:
    :return: возвращает список ссылок на страницы wiki
    """
    html_content = get_topic_page(topic)
    soup = BS(html_content, 'html.parser')
    li = soup.find_all('a')
    li2 = []
    for n in li:
        link = re.findall('https://[a-z]+.wikipedia.org/wiki/.+',n.get('href', ''))
        if len(link) > 0:
            li2.append(link[0])
    return li2


def get_page_subtopics(topic: str):
    """
    Возвращает все субтопики со страницы
    :param topic:
    :return: список убтопиков - которые сразу можно передавать на запрос новых страниц
    """
    links = get_page_links(topic)
    sub_topics = []
    for n in links:
        sub_topic = re.sub('https://[a-z]+.wikipedia.org/wiki/', '', n)
        sub_topics.append(sub_topic)
    return sub_topics
