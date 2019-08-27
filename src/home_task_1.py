try:
    num = int(input('Введите число:'))
    print(num + 2)
except ValueError:
    print('Введено не число')
