import sys
import os
import platform


def reverse_num(n: int) -> int:
    res = ''
    m = n
    mem = 0
    mem += sys.getsizeof(n)
    while n > 0:
        res += str(n % 10)
        mem += sys.getsizeof(res)
        n //= 10
    print(f'Памяти занято в функции reverse_num для числа {m}: {mem} байта')
    return res


def reverse_str(n: int) -> str:
    mem = 0
    mem += sys.getsizeof(n)
    res = ''.join(reversed(str(n)))
    mem += sys.getsizeof(res)
    print(f'Памяти занято в функции reverse_str для числа {n}: {mem} байта')
    return res


if __name__ == '__main__':
    num = 45326321
    print(reverse_num(num))
    print(reverse_str(num))
    print(f'os.name = {os.name}')
    print(f'platform.system = {platform.system()}')
    print(f'platform.release = {platform.release()}')
    print(f'sys.version = {sys.version}')


"""
Памяти занято в функции reverse_num для числа 45326321: 456 байта
12362354
Памяти занято в функции reverse_str для числа 45326321: 85 байта
12362354
os.name = posix
platform.system = Darwin
platform.release = 18.7.0
sys.version = 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)]

# python -m timeit -n 1000 -s "import les_4_htask_1_1" "les_4_htask_1_1.reverse_num(123456)"
# 1000 loops, best of 5: 3.16 usec per loop
# python -m timeit -n 1000 -s "import les_4_htask_1_1" "les_4_htask_1_1.reverse_str(123456)"
# 1000 loops, best of 5: 1.19 usec per loop

# python -m timeit -n 1000 -s "import les_4_htask_1_1" "les_4_htask_1_1.reverse_num(123456789)"
# 1000 loops, best of 5: 4.59 usec per loop
# python -m timeit -n 1000 -s "import les_4_htask_1_1" "les_4_htask_1_1.reverse_str(123456789)"
# 1000 loops, best of 5: 1.31 usec per loop

Для больших чисел переворот с помощью строки эффективнее
По памяти переворот с помощью методов строки намного эффективнее
По поддержке кода - лучше пользоваться встроенными библиотечными методами - они уже протестированы
"""
