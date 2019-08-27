while True:
    try:
        num = int(input('Введите число больше 0, но меньше 10:'))
    except ValueError:
        print('Введено не число')
        continue

    if 0 < num < 10:
        print('Ваше число', num, 'в степени 2 =', num**2)
        break
    else:
        print('введено неверное число')
        continue
