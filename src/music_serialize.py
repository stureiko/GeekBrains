# Создать модуль music_serialize.py. В этом модуле определить словарь для вашей
# любимой музыкальной группы, например:
#
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
#
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты,
# вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно.
# В файле group.json указать кодировку utf-8.

import pickle
import json

# Исходный объект для сериализации
my_favorite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний день осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
               {'name': 'Шапито', 'year': 2014}]}

# сериализация в байты
byte_my_favorite_group = pickle.dumps(my_favorite_group)

# Вывести в терминал
print(byte_my_favorite_group)
print(type(byte_my_favorite_group))

# Записать в файл picle
with open('groups_byte.picle', 'wb') as f:
    pickle.dump(byte_my_favorite_group, f)

# ************ Логичнее сразу записать в файл без промежуточного преобразования в байты *********
# но задание требует сначала преобразовать в байты

with open('groups.picle', 'wb') as f:
    pickle.dump(my_favorite_group, f)


# Сериализация в json
json_my_favorite_group = json.dumps(my_favorite_group)
print(json_my_favorite_group)
print(type(json_my_favorite_group))

# Запись в файл json
with open('groups_byte.json', 'w', encoding='utf-8') as f:
    json.dump(json_my_favorite_group, f)

# ************ Логичнее сразу записать в файл без промежуточного преобразования *********

with open('groups.json', 'w') as f:
    json.dump(my_favorite_group, f)
