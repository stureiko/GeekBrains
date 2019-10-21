a = int(input('Введите а: '))
b = int(input('Введите b: '))
c = int(input('Введите с: '))

if a > b:
    if a > c:
        print(f'max = {a}')
    else:
        print(f'max = {c}')
else:
    if b > c:
        print(f'Max = {b}')
    else:
        print(f'Max = {c}')
