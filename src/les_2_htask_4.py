"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.

************
Мне не нравится - порой матан - чему равна сумма членов такого ряда
"""

n = int(input('Введите колчество элементов ряда: '))
res = 0
for i in range(0, n):
    if i % 2 == 0:
        print(f'{i}, {1/(2**i)}')
        res += 1/(2**i)
    else:
        print(f'{i}, {-1/(2**i)}')
        res -= 1/(2**i)
print(res)