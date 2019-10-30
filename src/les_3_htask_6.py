"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

num = [random.randint(1, 100) for _ in range(10)]
pos_min = 0
n_min = 100
pos_max = 0
n_max = 0
sum = 0

for i in range(len(num)):
    if n_max < num[i]:
        n_max = num[i]
        pos_max = i
    if n_min > num[i]:
        n_min = num[i]
        pos_min = i

print(num)
print(f'min: {n_min}, position: {pos_min}')
print(f'max: {n_max}, position: {pos_max}')

if pos_min > pos_max:
    for i in range(pos_max+1, pos_min):
        sum += num[i]
elif pos_max > pos_min:
    for i in range(pos_min+1, pos_max):
        sum += num[i]
else:
    sum = num[pos_max]

print(sum)
