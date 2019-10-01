# https://ru.wikipedia.org/wiki/Дерево
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


if __name__ == '__main__':
    get_topic_page("дерево")

