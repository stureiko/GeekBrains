"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

import random

size = 20
array = [random.randint(0, 50) for _ in range(size)]


def sort_merge(array: list):
    if len(array) > 1:
        med = len(array) // 2
        left = array[:med]
        right = array[med:]

        sort_merge(left)
        sort_merge(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    print(array)
    sort_merge(array)
    print(array)
