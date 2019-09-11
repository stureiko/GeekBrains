# 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9
# в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки.
# Проверьте работу функций в этом же модуле.

import os

# Создаем директории по заданному шаблону
# Если такая папка уже существует - пропускаем, иначе os.mkdir - вылетит с ошибкой
def create_dir():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        if not os.path.exists(new_path):
            os.mkdir(new_path)
            print(f'Created: {new_path}')


# Удаляем диретории по заданному шаблону
# Проверяем: если такой директории нет - пропускаем, иначе os.rmdir - вылетит с ошибкой
def del_dir():
    for i in range(1, 10):
        del_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        if os.path.exists(del_path):
            os.rmdir(del_path)
            print(f'Deleted: {del_path}')


print('\nСоздаем')
create_dir()

print('\nУдаляем')
del_dir()

