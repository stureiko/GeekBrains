# Создать модуль music_deserialize.py.
# В этом модуле открыть файлы group.json и group.pickle,
# прочитать из них информацию.
# И получить объект: словарь из предыдущего задания.

import pickle
import json

# ************ Работа с picle **************
# Загрузить из файла байты
with open('groups_byte.picle', 'rb') as f:
    byte_my_favorite_groups = pickle.load(f)

# Преобразоваь в объект
my_favorite_groups = pickle.loads(byte_my_favorite_groups)
print(my_favorite_groups)

# Загрузить из файла сразу объект
with open('groups.picle', 'rb') as f:
    my_favorite_groups = pickle.load(f)
print(my_favorite_groups)

# ************* Работа с json **************
# Загрузить из файла
with open('groups_byte.json', 'r') as f:
    json_my_favorite_groups = json.load(f)

# Преобразовтаь в объект
my_favorite_groups = json.loads(json_my_favorite_groups)
print(my_favorite_groups)

# Загрузить из файла сразу объект
with open('groups.json', 'r') as f:
    my_favorite_groups = json.load(f)
print(my_favorite_groups)
