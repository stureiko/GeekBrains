num = int(input('Введите число: '))
ans = input('Введите признак: ').lower()
if ans == 'b':
    print(num * 1024)
elif ans == 'k':
    print(num / 1024)
else:
    print('Неправильный ввод')
