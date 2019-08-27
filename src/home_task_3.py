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

# Обрабатываем заключение в зависимости от условий
if user_age < 30 and 50 < user_weight < 120:
    print('хорошее состояние')
elif user_age > 30 and (user_weight < 50 or user_weight > 120):
    print('следует заняться собой')
elif user_age > 40 and (user_weight < 50 or user_weight > 120):
    print('следует обратиться к врачу!')
else:
    print('Все в порядке, нет рекомендаций.')
