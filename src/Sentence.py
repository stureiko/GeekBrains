"""
Класс слова, содержит слово и часть речи
"""
class World:
    text = ""
    part = ""

    def __init__(self, text, part):
        self.text = text
        self.part = part


# Создать слово
wd = World('test', 'глагол')


"""
Класс предложения
"""
class Sentence:
    content = []

    def __init__(self, li: list):  # конструктор инициализируемый списком
        self.content = li

    # Показать список слов на основании content[], список слов передается из вне
    def show(self, words: list):
        for i in self.content:
            if i < len(words):
                print(words[i].text, end=' ')
        print(end='\n')

    # Показать список частей речи на основании content[], список слов передается из вне
    def show_parts(self, words: list):
        part_set = set()  # Поскольку части речи должны упоминатося только один раз - то поместим их в множество
        for i in self.content:
            if i < len(words):
                part_set.add(words[i].part)  # дубликаты не будут включены, т.к part_set - множество
        for i in part_set:
            print(i, end=' ')
        print(end='\n')


# Список слов
words = [World('собака', 'сущ'),
         World('ела', 'глагол'),
         World('колбасу', 'сущ'),
         World('вечером', 'наречие')]

# список индексов для content
li = [0, 1, 2, 3, 4]

s = Sentence(li)
s.show(words)
s.show_parts(words)
