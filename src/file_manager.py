import os
import shutil
import datetime
import random


# функция создания файла
def create_file(filename, text=None):
    with open(filename, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


def get_list(path, folders_only=False):
    if path:
        try:
            result = os.listdir(path)
        except FileNotFoundError:
            print('Такого пути не найдено')
    else:
        result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# def get_list(folders_only=False):
#     result = os.listdir()
#     if folders_only:
#         result = [f for f in result if os.path.isdir(f)]
#     print(result)


def delete_f(name):
    if os.path.exists(name):
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)


def copy_f(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже существует')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time}: {message}'
    with open('log.log', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def play():
    number = random.randint(1, 100)
    user_number = None
    count = 0
    # Выбераем уровень сложности
    # делаем проверку на валидность ввода
    levels = {1: 10, 2: 5, 3: 3}
    while True:
        level = input('Введите уровень сложности от 1 до 3: ')
        if level.isdigit():
            if int(level) in levels.keys():
                print(f'Вы выбрали {int(level)} уровень')
                break
            else:
                print(f'Такого уровня не предусмотрено.')
                continue
        else:
            print('Вы ввели не число')
            continue

    max_count = levels[int(level)]

    while number != user_number:
        count += 1
        if count > max_count:
            print('Просрали !!!')
            break
        print(f'Попытка № {count}')
        user_number = input('Введите число от 1 до 100: ')
        if user_number.isdigit():
            user_number = int(user_number)
        else:
            print('Вы ввели не число. Попробуйте еще раз.')
            continue
        if number > user_number:
            print('Ваше число меньше загаданного.')
        elif number < user_number:
            print('Ваше число больше загаданного')
    else:
        print('Победа!')

if __name__ == '__main__':
    current_path = os.getcwd()
    get_list(True)
    delete_f('test')
    save_info('Test message')

