"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


def reverse_num(n: int) -> int:
    res = ''
    while n > 0:
        res += str(n % 10)
        n //= 10
    return res


def reverse_str(n: int) -> str:
    res = ''.join(reversed(str(n)))
    return res


if __name__ == '__main__':
    num = 45326
    print(reverse_num(num))
    print(reverse_str(num))


# python -m timeit -n 1000 -s "import les_4_htask_1_1" "les_4_htask_1_1.reverse_num(123456)"
# 1000 loops, best of 5: 3.16 usec per loop
# python -m timeit -n 1000 -s "import les_4_htask_1_1" "les_4_htask_1_1.reverse_str(123456)"
# 1000 loops, best of 5: 1.19 usec per loop

# python -m timeit -n 1000 -s "import les_4_htask_1_1" "les_4_htask_1_1.reverse_num(123456789)"
# 1000 loops, best of 5: 4.59 usec per loop
# python -m timeit -n 1000 -s "import les_4_htask_1_1" "les_4_htask_1_1.reverse_str(123456789)"
# 1000 loops, best of 5: 1.31 usec per loop

"""Для больших чисел переворот с помощью строки эффективнее"""

