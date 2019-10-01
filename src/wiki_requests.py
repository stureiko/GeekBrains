# https://ru.wikipedia.org/wiki/Дерево
import collections
import re
from requests import get
from bs4 import BeautifulSoup as BS


def get_link(topic: str):
    link = "https://ru.wikipedia.org/wiki/" + topic.capitalize()
    return link


def get_topic_page(topic: str):
    link = get_link(topic)
    html_content = get(link).text
    return html_content


def get_topic_words(topic):
    html_content = get_topic_page(topic)
    words = re.findall('[а-яА-Я\-\']{3,}', html_content)
    return words


def get_topic_text(topic):
    text = ' '.join(get_topic_words(topic))
    return text


def get_common_words(topic):
    words = get_topic_words(topic)
    rate = collections.Counter(words).most_common()
    return rate


def get_page_lincs(topic):
    html_content = get_topic_page(topic)
    soup = BS(html_content, 'html.parser')
    li = soup.find_all('a')
    li2 = []
    for n in li:
        li2.append(n.get('href', ''))
    return li2
