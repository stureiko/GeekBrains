num = int(input('Введите 3-х значное число: '))
a = num // 100
b = num % 100 // 10
c = num % 10
summa = a + b + c
mult = a * b * c
print(f'summa = {summa}, mult = {mult}')
