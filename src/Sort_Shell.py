import random

size = 3000
array = [i for i in range(size)]
random.shuffle(array)
# print(array)


def shell_sort(array: list):

    assert len(array) < 4000, 'Массив слишком велик, используйте другой метод сортировки'

    def new_increment(array: list) -> list:
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]

        while len(array) <= inc[-1]:
            inc.pop()

        while len(inc) > 0:
            yield inc.pop()

    count = 0
    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
                count += 1
    print(f'Number of steps: {count}')


shell_sort(array)
# print(array)
