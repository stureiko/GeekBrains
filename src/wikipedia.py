from wiki_requests import get_topic_page, get_topic_words, get_topic_text, get_common_words, get_page_lincs

if __name__ == '__main__':
    # topic = input('Введите тему запроса: ')
    # rate = get_common_words(topic)
    # for r in range(0, 9):
    #     print(rate[r][0] + ': ' + str(rate[r][1]))
    topic = 'дерево'
    print(get_page_lincs(topic))

