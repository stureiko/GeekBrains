import os
import shutil
import datetime


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


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


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


if __name__ == '__main__':
    current_path = os.getcwd()
    get_list(True)
    delete_f('test')
    save_info('Test message')
