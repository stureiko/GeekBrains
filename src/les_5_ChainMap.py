from collections import ChainMap


d_1 = {'a': 2, 'b': 4, 'c': 6}
d_2 = {'a': 10, 'b': 20, 'd': 40}

d_map = ChainMap(d_1, d_2)
print(d_map)

d_2['a'] = 100
print(d_map)

print('*' * 50)

x = d_map.new_child()  # добавили в начало новый словарь
print(x)

print(x.maps[0])  # первый словарь из коллекции
print(x.maps[-1])  # последний словарь из кллекции
