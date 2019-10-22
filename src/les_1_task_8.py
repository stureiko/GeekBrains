"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
"""
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a > c:
    if a < c:
        print(f'Average: {a}')
    else:
        if b > c:
            print(f'Average: {b}')
        else:
            print(f'Average: {c}')
else:
    if a > c:
        print(f'Average: {a}')
    else:
        if b > c:
            print(f'Average: {c}')
        else:
            print(f'Average: {b}')
