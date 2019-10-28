import random

array = [random.randint(-100, 100) for _ in range(10)]
print(f'Исходный массив {array}')

num = int(input('Какое число вставить: '))
pos = int(input('На какую позицию: '))

array.append(None)
i = len(array) - 1

while i > pos:
    array[i], array[i-1] = array[i-1], array[i]
    i -= 1

array[pos] = num
print(f'Новый масив: {array}')
