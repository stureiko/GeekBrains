a = int(input('Введите а: '))
b = int(input('Введите b: '))
c = int(input('Введите с: '))
m = a
if m < b:
    m = b
if m < c:
    m = c
print(f'Максимальное число {m}')
