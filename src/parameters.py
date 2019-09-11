import sys
import os

# print(f'Исполняемый файл: {sys.argv[0]}')
#
# print('\nНапечатаем все аргументы: ')
# for arg in sys.argv:
#     print(arg)


def ping():
    print('pong')


def hello(name):
    print('Hello', name)


def get_info():
    print(os.listdir())


command = sys.argv[1]
if command == 'ping':
    ping()
elif command == 'name':
    hello(sys.argv[2])
elif command == 'list':
    get_info()
