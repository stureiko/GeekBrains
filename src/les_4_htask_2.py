"""Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и
возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена»."""
import functools
import cProfile


def erat(n: int) -> []:
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):

        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]
    return result


@functools.lru_cache()
def eratosfen(n: int) -> int:
    result = erat(n)
    m = n
    while len(result) < n:
        m += 100
        result = erat(m)
    return result[n-1]


# cProfile.run('eratosfen(500)')

# 2    0.000    0.000    0.000    0.000 les_4_htask_2.py:10(erat)  10
# 3    0.000    0.000    0.000    0.000 les_4_htask_2.py:10(erat)  50
# 32    0.028    0.001    0.035    0.001 les_4_htask_2.py:10(erat) 500

"""Профилирование без использования lru_cache()"""
# "les_4_htask_2.eratosfen(10)"
# 1000 loops, best of 5: 41.9 usec per loop

# "les_4_htask_2.eratosfen(50)"
# 1000 loops, best of 5: 156 usec per loop

# "les_4_htask_2.eratosfen(100)"
# 1000 loops, best of 5: 811 usec per loop

# "les_4_htask_2.eratosfen(500)"
# 100 loops, best of 5: 28.7 msec per loop


"""Профилирование с использованием lru_cache()"""
# "les_4_htask_2.eratosfen(10)"
# 1000 loops, best of 5: 198 nsec per loop

# "les_4_htask_2.eratosfen(50)"
# 1000 loops, best of 5: 190 nsec per loop

# "les_4_htask_2.eratosfen(500)"
# 1000 loops, best of 5: 187 nsec per loop


def erat_loop(n: int) -> []:
    lst = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst


@functools.lru_cache()
def eratosfen_loop(n: int) -> int:
    result = erat_loop(n)
    m = n
    while len(result) < n:
        m += 100
        result = erat(m)
    return result[n-1]

"""Профилирование без использования lru_cache()"""
# "les_4_htask_2.eratosfen_loop(10)"
# 1000 loops, best of 5: 40.3 usec per loop

# "les_4_htask_2.eratosfen_loop(100)"
# 1000 loops, best of 5: 798 usec per loop

"""Профилирование с использованием lru_cache()"""
# "les_4_htask_2.eratosfen_loop(10)"
# 1000 loops, best of 5: 245 nsec per loop

# "les_4_htask_2.eratosfen_loop(50)"
# 1000 loops, best of 5: 187 nsec per loop

# "les_4_htask_2.eratosfen_loop(500)"
# 1000 loops, best of 5: 206 nsec per loop

""" С использованием lru_cache() разница при вычислении с сипользованием решета Эратосфена 
и перебора делителей не видна"""


