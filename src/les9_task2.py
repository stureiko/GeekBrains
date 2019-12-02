#    Задание № 2 урока № 9:
#    Закодируйте любую строку по алгоритму Хаффмана.

from collections import namedtuple

string = 'hello'

leaf = namedtuple('leaf', 'value, freq, code') # именованный кортеж - лист(значение, частота, код)
leafList = []
charList = list(set(string))
# print(charList)

for char in charList:
    leafList.append(leaf(char, 0, ''))
# print(leafList)

for char in string: # Подсчитываем частоту символов
    leafList[charList.index(char)] = leafList[charList.index(char)]._replace(
        freq=leafList[charList.index(char)].freq + 1)
# print(leafList)

leafList = sorted(leafList, key=lambda x: x.value, reverse=True) # Сортируем по символам
leafList = sorted(leafList, key=lambda x: x.freq) # Сортируем по частоте
# print(leafList)

charList.clear() # Вспомогательный список
for item in leafList:
    charList.append(item.value)

workList = leafList[:] # Делаем копию
# print(workList)

while len(workList) > 1: # сдесь суррогатный алгоритм для формирования кода, лень разбираться в обходе по бин. дереву,
                         # реализация алгоритма Хаффмана прям как он есть
    a, b = workList.pop(0), workList.pop(0)
    c = leaf(a.value + b.value, a.freq + b.freq, '')
    # print(a, b, c)

    for char in a.value:
        leafList[charList.index(char)] = leafList[charList.index(char)]._replace(
            code='0' + leafList[charList.index(char)].code)

    for char in b.value:
        leafList[charList.index(char)] = leafList[charList.index(char)]._replace(
            code='1' + leafList[charList.index(char)].code)

    for i, item in enumerate(workList):
        if item.freq >= c.freq:
            workList.insert(i, c)
            break
    else:
        workList.append(c)
    # print(workList)
# print(leafList)

for item in leafList:
    print(f'Символ "{item.value}" получил код - {item.code}')

s = ''
for char in string:
    s = s + leafList[charList.index(char)].code + ' '
print(f'Итоговый код строки "{string}" - {s}') # Код есть и соответствует видео-уроку, можно считать задачу выполненной,
                                               # для проверки правильности сравните на своих входных строках

# Вывод вида -  Символ "r" получил код - 1000
#               Символ "!" получил код - 1001
#               Символ "p" получил код - 101
#               Символ "o" получил код - 010
#               Символ " " получил код - 011
#               Символ "b" получил код - 00
#               Символ "e" получил код - 11
#               Итоговый код строки "beep boop beer!" - 00 11 11 101 011 00 010 010 101 011 00 11 11 1000 1001
#
#               Process finished with exit code 0
