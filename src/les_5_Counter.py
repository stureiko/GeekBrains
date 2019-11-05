from collections import Counter
import logging

# Создание Counter'ов

a = Counter()
b = Counter('abracadabrab')
c = Counter({'red': 2, 'blue': 4})
d = Counter(cats=4, dogs=5)

print(a, b,c, d, sep='\n')
print('*'*50+'\n')
print(list(b.elements()))  # Выведет элементы

print(b.most_common(2))  # Выведет два наиболее часто встречающиеся элемента
print('*'*50+'\n')
g = Counter(a=4, b=6, c=-2, d=0)
f = Counter(a=1, b=2, c=3, d=-2)
print(g)
print(f)
g.subtract(f)
print(g)
print('*'*50+'\n')

print(set(g))
print(dict(g))
print('*'*50+'\n')

x = Counter(a=3, b=1)
y = Counter(a=1, b=2)
print(x)
print(y)
print('\n')
print(x + y)
print(x - y)
print(x & y)
print(x | y)

print('*'*50+'\n')
z = Counter(a=1, b=-3)
print(+z)
print(-z)
