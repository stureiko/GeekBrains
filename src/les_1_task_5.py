"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
num = int(input('Введите номер буквы: '))
num_a = ord('a')
num_z = ord('z')

if (num + num_a - 1) in range(num_a, num_z + 1):
    print(f'Это буква: {chr(num_a + num - 1)}')
else:
    print('Это не буква алфавита')
