"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""


# ***** реализация через for
def find_loop(source: str, target: str) -> int:
    res = 0
    for i in source:
        if i == target:
            res += 1
    return res


# ***** реализация через метод строки
def find_str(source: str, target: str) -> int:
    res = source.count(target)
    return res

# python -m timeit -n 1000 -s "import les_4_htask_1_2" "les_4_htask_1_2.find_loop('12345678987654565', '5')"
# 1000 loops, best of 5: 1.31 usec per loop

# python -m timeit -n 1000 -s "import les_4_htask_1_2" "les_4_htask_1_2.find_str('12345678987654565', '5')"
# 1000 loops, best of 5: 424 nsec per loop

"""Использование встроенных методов строк эффективнее"""
