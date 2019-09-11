import os
import sys

print('\n***************** Работа с модулем os *****************')
print(f'Операционная система: {os.name}')
print(f'Текущая директория: {os.getcwd()}')
# создаем новый путь
new_path = os.path.join(os.getcwd(), 'new_f')
if not os.path.exists(new_path):
    # создаем папку по указанному пути
    os.mkdir(new_path)
else:
    print(f'Такой путь уже существует: {new_path}')

print('\n\n***************** Работа с модулем sys *****************')
print(f'Путь до интерпретатора Python: {sys.executable}')
print(f'Платформа {sys.platform}')

# принудительное завершение программы - c указанием кода выхода
# sys.exit(2)

for path in sys.path:
    print(path)

# Добавить в sys.path путь к модулям
# sys.path.append('путь')

# ***************** Создаем в текущей директории папки ******************
name = sys.platform
for i in range(1, 6):
    new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
    if not os.path.exists(new_path):
        # создаем папку по указанному пути
        os.mkdir(new_path)
