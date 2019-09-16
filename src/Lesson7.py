import random

# Тернарный оператор
# результат 1 если условие иначе результат 2
print('\n*************** Тернарный оператор ****************')
print('Возвращаем истину')
condition = True
print('Max' if condition else 'Min')

print('Возвращаем ложь')
condition = False
print('Max' if condition else 'Min')

# слово -> СлОвО
word = 'слово'
result = []

for i in range(len(word)):
    letter = word[i]
    letter = letter.lower() if i % 2 != 0 else letter.upper()
    result.append(letter)

result = ''.join(result)
print(result)

# **************** Генераторы **********************
print('\n*************** Генераторы ****************')
numbers = [1, 2, 3, 4, 5, -1, -2, -3]
result = [number for number in numbers if number > 0]
print(result)

# список из 10 случайных чисел
numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

# списко квадратов чисел из списка
numbers = [-2, 4, 2, 9, 4, 5]
squares = [number**2 for number in numbers]
print(squares)

# имена на букву 'А' из списка
names = ['Андрей', 'Борис', 'Алексей', 'Денис']
a_names = [name for name in names if name.startswith('А')]
print(a_names)

# Приведение к логическому условию
print('\n*************** Приведение к логическому типу ****************')
str = 'test string'
print(str)
print('Строка не пустая' if str else 'Строка пустая')

str = ''
print(str)
print('Строка не пустая' if str else 'Строка пустая')

print('\n*************** and возвращает последнюю истину ****************')
print([1] and 1 and 20 and 1.2)

print('\n*************** or возвращает последнюю ложь или первую истину ****************')
print([1] or [])
print([] or '' or {})

print('\n*************** Применение логики **************')
print('Выввести из  списка числа, корень из которых больше 2')

import math
numbers = [1, 2, 3, 4, 6, 8, -8, -4, -9]
numbers = [number for number in numbers if number > 0 and math.sqrt(number) > 2]
print(numbers)

print('\nДобавление в список элемента, если список передан на вход')


def add_to_list(input_list=None):
    input_list = input_list or []
    input_list.append(2)
    return input_list


print('Пустой список')
print(add_to_list())

print('Не пустой список')
print(add_to_list([0, 1]))

print('\nКопирование списков')
# для одноуровневых списков можно использоват срез или copy
a = [1, 2, 3]
b = a[:]
b[1] = 100
print(a)  # а не поменялся

b = a.copy()
b[1] = 200
print(a)  # а не поменялся

a = [1, 2, [3, 4]]
b = a.copy()
b[2][1] = 200
print(a)  # a поменялся !!!

import copy
print('Используем deepcopy()')
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
b[2][1] = 200
print(a)  # а не поменялся !!!
