# import random
#
# numbers = []
# number = ''
# for i in range(3):
#     while not number.isdigit():
#         number = input(f'Введите число № {i+1}: ')
#     else:
#         numbers.append(int(number))
#         number = ''
#
# print(numbers)
# print(f'Максимум {max(numbers)}')
# print(f'Мининум {min(numbers)}')
# print(f'Сумма {sum(numbers)}')


def print_sep():
    print('-*' * 50)


print_sep()


def print_sep(sep):
    print(sep * 50)


print_sep('*')


def print_sep(sep, sep_len):
    print(sep * sep_len)


print_sep('-', 55)


def print_sep(sep, sep_len):
    return sep * sep_len


print(print_sep('*', 50))


def hello_max():
    print('Hello', 'Max')


hello_max()


def hello(name):
    print('Hello', name)


hello('Max')


def greeting(name, say='Hello'):
    print(say, name)


greeting('Leo', 'Hi')

greeting('Max')

# ******** Передача произвольного количетва параметров ************


def greeting(say='Hello', *args):
    print(say, args)


greeting('Hi', 'Max', 'Leo')


# ******** Передача произвольного количетва параметров по имени ************

def get_person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


get_person(name='Max', age=20, car="Lexus")

# ******** Задание типа аргумента функции ************

def any_person(s: dict):
    for k in s.keys():
        print(s[k])


friend = {'name': 'Max', 'age': 23}

any_person(friend)


# ******** Глобальные переменные ************
print('\n******** Глобальные переменные ************')
global_var = 1


def my_func():
    global global_var
    print(global_var)
    global_var = 3


my_func()
print(global_var)


# ******** Функции как параметр ************
print('\n\n******** Функции как параметр ************')

# ******** Функция фильтрации ************


def my_filter(numbers: list, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result


def is_even(number):
    return number % 2 == 0


print('\n******** Вывести четные числа ************')

numbers = range(1, 9)
print(my_filter(numbers, is_even))

print('\n******** Вывести нечетные числа ************')

def non_even(number):
    return number % 2 != 0


print(my_filter(numbers, non_even))


print('\n\n******** Применение lambda функций ************')
print('******** Вывести нечетные числа ************')
print(my_filter(numbers, lambda num: num % 2 != 0))


print('\n\n******** Применение sorted ************')
numbers = [1, 3, 4, 2, 6, 9, 8, 11]
print('Сортировка по возрастанию')
print(sorted(numbers))

print('\nСортировка по убыванию')
print(sorted(numbers, reverse=True))

print('\nСортировка по алфавиту')
cities = [('Москва', 1000), ('Лас-Вегас', 2000), ('Антверпен', 500)]
print(sorted(cities))

print('\nСортировка по значению')


def by_count(city: tuple):
    return city[1]


print(sorted(cities, key=by_count))

print('\n\n******** Применение filter ************')
numbers = (1, 3, 4, 2, 6, 9, 8, 11)

print(list(filter(is_even, numbers)))


names = ['Max', 'Leo', 'Kate']
print(list(filter(lambda name: len(name) > 3, names)))


print('\n\n******** Применение map ************')
# применяет функцию к каждому элементу последовательности

print(numbers)
print(tuple(map(lambda x: x**2, numbers)))