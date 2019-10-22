"""
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

let1 = input('Введите первую букву: ')
let2 = input('Введите вторую букву: ')
num1 = ord(let1)
num2 = ord(let2)

num_a = ord('a')
num_z = ord('z')

if num1 in range(num_a, num_z + 1) and num2 in range(num_a, num_z + 1):
    print(f'Позиция символа {let1} = {num1 - num_a + 1}')
    print(f'Позиция символа {let2} = {num2 - num_a + 1}')

    if num1 > num2:
        print(f'Между ними {num1 - num2 - 1} символов')
    elif num1 < num2:
        print(f'Между ними {num2 - num1 - 1} символов')
    else:
        print(f'Между ними 0 символов')
else:
    print('Введены не буквы алфавита')
