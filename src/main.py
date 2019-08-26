print('Hello World!')

ale = 71
age = int(input('Сколько вам лет: '))

after20 = age + 20
print('Через 20 лет вам будет:', after20)

alive = ale - age
print('Вам осталось жить:', alive, 'лет.')

count = age*365*24*60
print('Вы прожили', count, 'секунд.\n')

if age < 18:
    print('Доступ запрещен!')
else:
    print('Доступ разрешен!')

num = 0

while num <= age:
    if num % 2 ==0:
        print(num)
    num += 1
