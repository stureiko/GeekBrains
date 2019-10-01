# https://ru.wikipedia.org/wiki/Дерево
import re
from requests import get


def get_link(topic: str):
    link = "https://ru.wikipedia.org/wiki/" + topic.capitalize()
    return link


def get_topic_page(topic: str):
    link = get_link(topic)
    html_content = get(link).text
    # with open(topic+".html", "w", encoding="utf-8") as f:
    #     f.write(html_content)
    return html_content


def get_topic_words(topic):
    html_content = get_topic_page(topic)
    words = re.findall('[а-яА-Я]+', html_content)
    return words


def get_topic_text(topic):
    text = ' '.join(get_topic_words(topic))
    return text


if __name__ == '__main__':
    get_topic_page("дерево")

