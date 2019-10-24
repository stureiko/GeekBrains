"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
"""


while True:
    while True:
        n1 = input('Введите первое число: ')
        if n1.isdigit():
            n1 = float(n1)
            break
        else:
            print('Вы ввели не число, попробуйте еще раз.')
    while True:
        n2 = input('Введите второе число: ')
        if n2.isdigit():
            n2 = float(n2)
            break
        else:
            print('Вы ввели не число, попробуйте еще раз.')
    while True:
        oper = input('Введите операцию (+, -, *, /), для выхода введите 0:')
        if oper == '+' or oper != '-' or oper != '*' or oper != '/' or oper != '0':
            break
        else:
            print('Вы ввели недопустимую операцию, попробуйте еще раз')
    if oper == '0':
        print('Работа завершена')
        break
    else:
        print('Выполнение вычислений:')
        if oper == '+':
            print(f'{n1} + {n2} = {n1 + n2}')
        elif oper == '-':
            print(f'{n1} - {n2} = {n1 - n2}')
        elif oper == '*':
            print(f'{n1} * {n2} = {n1 * n2}')
        else:
            if n2 == 0:
                while True:
                    print('Делитель не может быть равен 0!')
                    n2 = input('Введите второе число: ')
                    if n2.isdigit():
                        n2 = float(n2)
                        if n2 != 0:
                            break
                    else:
                        print('Вы ввели не число или 0, попробуйте еще раз.')
            print(f'{n1} / {n2} = {n1 / n2}')
