# 2: Создайте модуль. В нем создайте функцию, которая принимает список
# и возвращает из него случайный элемент.
# Если список пустой функция должна вернуть None.
# Проверьте работу функций в этом же модуле.
#
#     Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]

import random


# проверяем последовательность - для пустой возвращаем None
# для не пустой выдергиваем случайный элемент
def random_arg(original_list: list):
    if len(original_list) == 0:
        return None
    else:
        return random.choice(original_list)


if (__name__) == '__main__':
    # генерируем списки для работы
    numbers = []
    for i in range(20):
        numbers.append(random.randint(-100, 100))
    num_non = []

    # проверяем работу
    print(random_arg(numbers))
    print(random_arg(num_non))

    #     Примечание: Список для проверки введите вручную.
    print('\n\nВвод тестового списка')
    numbers.clear()
    while True:
        num_items = input('Введите количество элементов тестового списка: ')
        try:
            num_items = int(num_items)
            if num_items > 0:
                break
            else:
                print('Необходимо ввести целое положительное число')
        except ValueError:
            print('Необходимо ввести целое положительное число')

    for i in range(1, num_items+1):
        while True:
            number = input(f'Введите {i}-й элемент списка: ')
            try:
                number = int(number)
                numbers.append(number)
                break
            except ValueError:
                print('Необходимо ввести целое число')

    print(random_arg(numbers))
