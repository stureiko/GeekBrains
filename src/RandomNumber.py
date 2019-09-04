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
            print(f'Вы выбрали {int(level)} уровень')
            break
        else:
            print(f'Такого уровня не предусмотрено.')
            continue
    else:
        print('Вы ввели не число')
        continue

max_count = levels[3]

while number != user_number:
    count += 1
    if count > max_count:
        print('Просрали !!!')
        break
    print(f'Попытка № {count}')
    user_number = input('Введите число от 1 до 100: ')
    if user_number.isdigit():
        user_number = int(user_number)
    else:
        print('Вы ввели не число. Попробуйте еще раз.')
        continue
    if number > user_number:
        print('Ваше число меньше загаданного.')
    elif number < user_number:
        print('Ваше число больше загаданного')
else:
    print('Победа!')
