"""
Класс слова, содержит слово и часть речи
"""
class World:

    def __init__(self, text, part):
        self.text = text
        self.part = part


class Noun(World):
    __grammar: str = 'сущ'

    def __init__(self, text=''):
        self.text = text

    def part(self):
        return 'существительное'


class Verb(World):
    __grammar: str = 'гл'

    def __init__(self, text=''):
        self.text = text

    def part(self):
        return 'глагол'


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
                part_set.add(words[i].part())  # дубликаты не будут включены, т.к part_set - множество
        for i in part_set:
            print(i, end=' ')
        print(end='\n')


# Список слов
words = []
words.append(Noun("собака"))
words.append(Verb("ела"))
words.append(Noun("колбасу"))
words.append(Noun("кот"))
words.append(Verb('пошел'))


# список индексов для content
li = [0, 1, 2, 3, 4]

s = Sentence(li)
s.show(words)
s.show_parts(words)

