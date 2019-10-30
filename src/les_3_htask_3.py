"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
"""

import random

num = [random.randint(1, 100) for _ in range(10)]
pos_min = 0
n_min = 100
pos_max = 0
n_max = 0

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

print('Change elements:')
num[pos_min], num[pos_max] = num[pos_max], num[pos_min]
print(num)
