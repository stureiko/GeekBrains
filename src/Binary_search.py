import random


def bin_search(array: list, value: int) -> int:
    left = 0
    right = len(array) - 1
    pos = right // 2

    while array[pos] != value and left <= right:

        if value > array[pos]:
            left = pos + 1
        else:
            right = pos - 1

        pos = (left + right) // 2

    return -1 if left > right else pos


if __name__ == '__main__':
    a = [random.randint(0, 1000) for _ in range(100)]
    a.sort()
    print(f'Исходный массив {a}')
    n = int(input('Что ищем: '))
    print(f'Ищем {n}, это позиция {bin_search(a, n)}')
