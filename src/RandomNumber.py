import random

number = random.randint(1, 100)

while True:
    user_number = input('Введите число: ')
    if user_number.isdigit():
        user_number = int(user_number)
    else:
        print('Вы ввели не число. Попробуйте еще раз.')
        continue
    if number == user_number:
        print('Победа!')
        break
    elif number > user_number:
        print('Ваше число меньше загаданного.')
    else:
        print('Ваше число больше загаданного')