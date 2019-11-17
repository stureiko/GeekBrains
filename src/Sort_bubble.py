import random

size = 10
array = [i for i in range(size)]
# random.shuffle(array)
# print(array)


def sort_bubble(array):
    flag = False
    n = 1
    while n < len(array):
        if not flag:
            flag = True
            print(array)
            for i in range(len(array) - n):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    flag = False
            n += 1
        else:
            break


sort_bubble(array)
print(array)

