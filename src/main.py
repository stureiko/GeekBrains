# В консольный файловый менеджер добавить проверку ввода пользователя для всех функции
# с параметрами (на уроке разбирали на примере одной функции).

import sys
import os
from file_manager import create_file, create_folder, get_list, delete_f, copy_f, save_info, play


def main_work(arg):
    try:
        command = arg[0]
    except IndexError:
        command = 'help'

    save_info(f'Аргумент: {command}')

    if command == 'list':
        try:
            path = arg[1]
        except IndexError:
            path = ''
        get_list(path)
    elif command == 'create_file':
        try:  # проверяем наличие имени файла
            name = arg[1]
        except IndexError:
            print('Отсутствует имя файла')
        else:
            try:
                text = arg[2]  # проверяем наличие текста для записи в файл
                create_file(name, text)  # создаем файл с текстом
            except IndexError:  # если текста нет
                create_file(name)  # тогда просто создаем пустой файл
    elif command == 'create_folder':
        try:
            name = arg[1]  # если есть имя папки
        except IndexError:
            print('Отсутствует имя файла')
        else:
            create_folder(name)  # создаем папку с переданным именем
    elif command == 'delete':
        try:
            name = arg[1]  # если передано имя папки или файла
        except IndexError:
            print('Отсутствует имя файла')
        else:
            delete_f(name)  # удаляем указанную папку
    elif command == 'copy':
        try:  # для копирования должны присутствоват как имя копируемого объекта
            name = arg[1]  # так и имя нового объекта
            new_name = arg[2]
        except IndexError:
            print('Отсутствует имя файла')
        else:
            copy_f(name, new_name)
    elif command == 'play':
        play()
    else:
        print('i - переход в интерактивный режим')
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('play - игра \"Угадай число\"')
        print('help - список команд')
    save_info('завершение')


save_info('Запуск')

# print(sys.argv)

if len(sys.argv) < 2:
    arguments = 'help'
else:
    arguments = sys.argv[1:]

if arguments[0] == 'i':
    print('Интерактивный режим')
    while True:
        arguments = input('Введите команду: ').split()
        if len(arguments) == 0:
            arguments.append('help')
        else:
            if arguments[0] == 'exit':
                break
        # print(arguments)
        main_work(arguments)
else:
    main_work(arguments)

