"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
"""
from collections import OrderedDict, deque


h1 = '1A'
h2 = '1DF'



dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
        'D': 13, 'E': 14, 'F': 15}
hex_dict = OrderedDict(dict)
dict_n = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': 'A',
          '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
int_dict = OrderedDict(dict_n)


# Сложение 2-х строк в виде 16-ти ричных чисел
def plus(s1: str, s2: str) -> str:
    if s1 == '0' or s1 == '':
        return s2
    elif s2 == '0' or s2 == '':
        return s1
    elif len(s1) >= len(s2):

        spam = 0
        res = []
        s1 = s1[::-1]
        s2 = s2[::-1]
        i = 0
        for n in s1:
            if i < len(s2):
                num = hex_dict[s1[i]] + hex_dict[s2[i]] + spam
                spam = 0

                if num > 15:
                    num -= 16
                    spam += 1

                res.append(int_dict[str(num)])
                i += 1
            else:
                if hex_dict[n] + spam > 15:
                    res.append(int_dict[hex_dict[n] + spam - 15])
                    spam = 0
                    res.append('1')
                else:
                    res.append(int_dict[str(hex_dict[n] + spam)])
                    spam = 0
                i += 1

        return ''.join(reversed(res))
    else:
        return plus(s2, s1)


# Сложение 2-х строк в виде 16-ти ричных чисел через перевод их в десятичные
def int_plus(s1: str, s2: str) -> str:
    return my_int_to_hex(my_hex_to_int(s1) + my_hex_to_int(s2))


# Умножение 2-х строк в виде 16-ти ричных чисел через перевод их в десятичные
def int_mult(s1: str, s2: str) -> str:
    return my_int_to_hex(my_hex_to_int(s1) * my_hex_to_int(s2))


# Перевод 16-ти ричной строки в 10-ичную
def my_hex_to_int(s1: str) -> int:
    res = 0
    i = 0
    for n in s1[::-1]:
        num = hex_dict[n]
        res += num*(16**i)
        i += 1
    return res


# Перевод 10-ичного числа в 16-ричную строку
def my_int_to_hex(n1: int) -> str:
    d = deque()
    while n1 > 16:
        spam = n1 % 16
        d.appendleft(int_dict[str(spam)])
        n1 = n1 // 16
    spam = n1 % 16
    d.appendleft(int_dict[str(spam)])
    return ''.join(d)


if __name__ == '__main__':
    print(f'Исходные числа: h1 = {h1}, h2 = {h2}')
    print(f'Сумма (сложение в столбик) h1 + h2 = {plus(h1, h2)}')
    print(f'Сумма (сложение c переводом в 10) h1 + h2 = {int_plus(h1, h2)}')
    print(f'Произведение (c переводом в 10) h1 * h2 = {int_mult(h1, h2)}')



