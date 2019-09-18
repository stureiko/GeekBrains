# В консольный файловый менеджер добавить проверку ввода пользователя для всех функции
# с параметрами (на уроке разбирали на примере одной функции).

import sys
from file_manager import create_file, create_folder, get_list, delete_f, copy_f, save_info

save_info('Запуск')

try:
    command = sys.argv[1]
except IndexError:
    command = 'help'

save_info(f'Аргумент: {command}')

if command == 'list':
    get_list()
elif command == 'create_file':
    try:  # проверяем наличие имени файла
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует имя файла')
    else:
        try:
            text = sys.argv[3]  # проверяем наличие текста для записи в файл
            create_file(name, text)  # создаем файл с текстом
        except IndexError:  # если текста нет
            create_file(name)  # тогда просто создаем пустой файл
elif command == 'create_folder':
    try:
        name = sys.argv[2]  # если есть имя папки
    except IndexError:
        print('Отсутствует имя файла')
    else:
        create_folder(name)  # создаем папку с переданным именем
elif command == 'delete':
    try:
        name = sys.argv[2]  # если передано имя папки или файла
    except IndexError:
        print('Отсутствует имя файла')
    else:
        delete_f(name)  # удаляем указанную папку
elif command == 'copy':
    try:  # для копирования должны присутствоват как имя копируемого объекта
        name = sys.argv[2]  # так и имя новогообъекта
        new_name = sys.argv[3]
    except IndexError:
        print('Отсутствует имя файла')
    else:
        copy_f(name, new_name)
else:
    print('list - список файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')
