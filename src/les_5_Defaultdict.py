from collections import defaultdict, Counter

a = defaultdict()
print(a)

s = 'dhbsvblkbcblakbclbdvbadsjbvlkcbs;bdv;'
b = defaultdict(int)  # посчитаь тколичество вхождений

for i in s:
    b[i] += 1

print(b)
print(Counter(b).most_common(3))  # получить первые 3 позиции наиболее частое вхождение

list_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
c = defaultdict(list) # собрать списки значений

for k, v in list_1:
    c[k].append(v)

print(c)

list_2 = [('cat', 1), ('dog', 5), ('cat', 2), ('cat', 1), ('dog', 5)]
d = defaultdict(set)  # собрать списки только уникальных значений
for k, v in list_2:
    d[k].add(v)

print(d)


f = defaultdict(lambda: 'unknown')
f.update(rex='dog', tomas='cat')
print(f)
print(f['rex'])
print(f['jerry'])
