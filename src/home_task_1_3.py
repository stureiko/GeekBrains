"""
3 Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные:
имя, фамилия, возраст и вес.

Выведите результат согласно которому:

Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.

(Формула не соответствует реальной действительности и здесь используется только ради примера)

Примечание: при написание программы обратите внимание на условия в задаче и в вашем коде.
Протестируйте программу несколько раз и убедитесь, что проверки срабатывают верно.
В случае ошибок, уточните условия для той или иной ситуации.

Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

:autor: Stureiko Igor
:raise: ValueError
"""
print('Анкета')
# Читаем пользовательские данные
user_name = input('Введите ваше имя: ')
user_surname = input('Введите вашу фамилию: ')
# Возраст и вес должны быть цифрами (int) и быть > 0
# проверяем пользовательский ввод и в случае ошибки просим повторить
while True:
    # Перехватываем исключение в случае ввода не числа
    try:
        user_age = int(input('Введите ваш возраст: '))
        # в случае числа проверям на условие > 0
        if user_age < 1:
            print('Возраст должен быть положительным числом! Попробуйте еще раз.')
            continue
        break
    except ValueError:
        print('Возраст должен быть числом! Попробуйте еще раз.')
        continue

while True:
    try:
        user_weight = int(input('Введите ваш вес: '))
        if user_weight < 1:
            print('Вес должен быть положительным числом! Попробуйте еще раз.')
            continue
        break
    except ValueError:
        print('Вес должен быть числом! Попробуйте еще раз.')
        continue

# Формируем вывод данных. Постоянную часть
print(user_name, ' ', user_surname, ',', sep='', end=' ')

# Обрабатываем окончания (год, года, лет) в зависимости от возраста
last_num = user_age % 10
if last_num == 1:
    print(user_age, 'год, вес', user_weight, '-', end=' ')
elif last_num == 2 or last_num == 3 or last_num == 4:
    print(user_age, 'года, вес', user_weight, '-', end=' ')
else:
    print(user_age, 'лет, вес', user_weight, '-', end=' ')

# Обрабатываем переменную часть в зависимости от условий
if user_age < 30 and 50 < user_weight < 120:
    print('хорошее состояние')
elif user_age > 30 and (user_weight < 50 or user_weight > 120):
    print('следует заняться собой')
elif user_age > 40 and (user_weight < 50 or user_weight > 120):
    print('следует обратиться к врачу!')
else:
    print('Все в порядке, нет рекомендаций.')