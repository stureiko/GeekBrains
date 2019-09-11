print('Hello World!')
print('Lesson 2')
# работа со строками
print('\n\n**************** РАБОТА СО СТРОКАМИ *******************\n')
friend = 'Maxim Leonid'
print(friend)
print(friend[1])

print('\nРазделить строку на список слов')
print(friend.split())  # разделить строку на список слов
print('\nПосчитать количество слов в строке')
print(len(friend.split()))  # количество элементов в списке

print('\nпроверка на числовое значение - возвращает boolean')
num = '123'
print('num = {}'.format(num))
print('num это число? - {}'.format(num.isdigit()))

print('\nОбработка строки')
top5 = 'Первые 5 мест на соревнованиях 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов'
start = top5.find('1.')
end = top5.find('4.')

top3 = top5[start: end]

print('Поздравляем! {}'.format(top3))

# работа со списками
print('\n\n**************** РАБОТА СО СПИСКАМИ *******************\n')
# исходный список
friends = ['Max', 'Leo', 'Kate']

print('Исходный список: {}'.format(friends))
print('Длина списка: {}'.format(len(friends)))

# добавить элемент в конец списка
friends.append('Ron')
print('\nДобавить элемент в конец списка: {}'.format(friends))

# удалить последний элемент
print('\nУдалить последний элемент {}. Внимание! Возвращается СТРОКА!'.format(friends.pop()))
print('список стал: {}'.format(friends))

# удалить элемент по значению
print('\nУдалить элемент по значению. Удаляем элемент Leo.')
friends.remove('Leo')
print(friends)

print('\nУдалить элемент по индексу. Удаляем первый элемент - индекс = 0.')
# удалить элемент спсика по индексу
del friends[0]
print(friends)

# проверить вхождение - возвращает boolean
print('\nПроверить вхождение элемента Leo в список')
friends = ['Max', 'Leo', 'Kate']
print('Исходный список: {}'.format(friends))
print('Leo' in friends)

print('\nМожно использовать кортежи')
print('frends_fix = (\'Max\', \'Leo\', \'Kate\')')
friends_fix = ('Max', 'Leo', 'Kate')
print(friends_fix)

print('\n\n**************** РАБОТА С for *******************\n')
print('Исходный список: {}'.format(friends))
print('Вывести элементы:')
for friend in friends:
    print(friend)

print('То же для строки: {}'.format(friends[2]))
for letter in friends[2]:
    print(letter)

print('\n\n**************** РАБОТА С range *******************\n')
print(list(range(1, 20, 2)))

# либо

for i in range(1, 20, 2):
    print(i)

print('\n\n**************** РАБОТА СО СЛОВАРЕМ *******************\n')
friend = {'name': 'Max', 'age': 23}
print('Создание словаря: {}'.format(friend))
print(type(friend))

print('\nДоступ по ключу')
print('Сколько лет: {}'.format(friend['age']))

print('\nДобавление поля')
friend['has_car'] = True
print(friend)

print('\nУдаление по ключу')
del friend['age']
print(friend)

print('\nПроверка наличия ключа в словаре')
if 'has_car' in friend:
    print('Есть машина')

print('\nПеребор словаря')
print('\nПеребор по ключам')
friend['age'] = 23
for key in friend.keys():
    print(key)

# !!! Можно не указывать keys - это дефолтное поведение
print('\nПеребор по ключам по дефолту')
for key in friend:
    print(key)

print('\nПеребор по значениям')
for val in friend.values():
    print(val)

print('\nПолучение пары')
for item in friend.items():
    print(item)

print('\nПолучение отдельных значений ключ - значение')
for key, val in friend.items():
    print('{}: {}'.format(key, val))

print('\n\n**************** РАБОТА С МНОЖЕСТВАМИ *******************\n')
cities = {'Vegas', 'Moscow', 'Paris'}
print('Исходное множество:')
print(cities)

print('\nПриведение списка к множеству')
cit = ['Vegas', 'Moscow', 'Paris', 'Moscow']
print('Список: {}'.format(cit))
print('\nПриводим его к множеству просто через приведение типов: {}'.format(set(cit)))

print('\nДобавление элемента')
cities.add('Burma')
print(cities)

print('\nУдаление элемента')
cities.remove('Moscow')
print(cities)

print('\nОперации со множествами')
# Max взял вещи
max_things = {'Телефон', 'Бритва', 'Шорты', 'Рубашка'}
kate_things = {'Телефон', 'Зонтик', 'Шорты', 'Помада'}

# Какие все уникальные вещи взяли - объединение множеств

print('Уникальные вещи: {}'.format(max_things | kate_things))

# Какие вещи повторяются - пересечение множеств
print('Повторяющиеся вещи: {}'.format(max_things & kate_things))

# Какие вещи взяла Kate, но не взял Max
print('Вещи взяла Kate, но не взял Max: {}'.format(kate_things - max_things))
