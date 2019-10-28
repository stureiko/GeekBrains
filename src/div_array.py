import random

array = [random.randint(-100, 100) for _ in range(100)]

print(f'Исходный массив {array}')

arr_negative = []
arr_positive = []

for item in array:

    if item >= 0:
        arr_positive.append(item)
    else:
        arr_negative.append(item)

print(f'Положительные: {arr_positive}')
print(f'Отрицательные {arr_negative}')
