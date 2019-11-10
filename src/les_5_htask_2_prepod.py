"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
"""

from collections import deque

bin_numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
              'C': 12, 'D': 13, 'E': 14, 'F': 15}
hex_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def convert(hex_num: str):
    return deque(hex_num.upper())


def sum_hex(first, second):
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque()
    overflow = 0

    for i in range(len(first) - 1, -1, -1):
        first_num = bin_numbers[first[i]]
        second_num = bin_numbers[second[i]]

        result_num = first_num + second_num + overflow

        if result_num > 16:
            overflow = 1
            result_num -= 16
        else:
            overflow = 0

        result.appendleft(hex_number(result_num))
    if overflow == 1:
        result.appendleft('1')

    return result


def mult_hex(first, second):
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque('0')

    for i in range(len(first) - 1, -1, -1):
        second_num = bin_numbers[second[i]]

        spam = deque('0')

        for _ in range(second_num):
            spam = sum_hex(spam, first)

        spam.extend('0' * (len(first - i - 1)))

        result = sum_hex(result, spam)
    return result
