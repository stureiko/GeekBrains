import random

number = random.randint(1, 100)

user_number = None
count = 0
# Выбераем уровень сложности
# делаем проверку на валидность ввода
levels = {1: 10, 2: 5, 3: 3}


while True:
    level = input('Введите уровень сложности от 1 до 3: ')
    if level.isdigit():
        if int(level) in levels.keys():
            level = int(level)
            print(f'Вы выбрали {level} уровень, у вас {levels[level]} попыток.')
            break
        else:
            print(f'Такого уровня не предусмотрено.')
            continue
    else:
        print('Вы ввели не число')
        continue

max_count = levels[level]
user_count = None

while True:
    user_count = input('Введите количество пользователей: ')
    if user_count.isdigit():
        user_count = int(user_count)
        print(f'Вы ввели {user_count} пользователей.')
        break
    else:
        print('Вы ввели не число')
        continue

users = {}
for i in range(1, user_count+1):
    users[i] = input(f'Введите имя пользователя № {i}: ')

print('\nПользователи:')
for key, val in users.items():
    print(f'{key}: {val}')

print('\n')

is_winner = False
winner_name = ''

while not is_winner:
    count += 1
    if count > max_count:
        print('Просрали !!!')
        break
    print(f'Попытка № {count}')

    for key in users.keys():
        print(f'Ход пользователя {users[key]}')

        user_number = input('Введите число от 1 до 100: ')

        if user_number.isdigit():
            user_number = int(user_number)
        else:
            print('Вы ввели не число. Попробуйте еще раз.')

        if number == user_number:
            is_winner = True
            winner_name = users[key]
            break
        elif number > user_number:
            print('Ваше число меньше загаданного.')
        else:
            print('Ваше число больше загаданного')
else:
    print(f'Победитель {winner_name}!')
