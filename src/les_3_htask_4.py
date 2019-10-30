"""Определить, какое число в массиве встречается чаще всего."""

import random

num_size = 100
num = [random.randint(1, 10) for _ in range(num_size)]
res = {}

for i in num:
    if i in res.keys():
        res[i] += 1
    else:
        res.update({i: 1})

n_res = 0
pos_res = 0

for i in res.keys():
    if n_res < res[i]:
        n_res = res[i]
        pos_res = i

print(pos_res)
