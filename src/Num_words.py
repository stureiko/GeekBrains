import re
import collections

# Читаем из файла текст для разбора
try:
    with open('text.txt', 'r') as f:
        text = f.read()
except FileNotFoundError:
    print('Файл не найден')
    text = ''

print('\nРазделить на предложения. Согласно заданию предложения отделяются . ! или ?')
li2 = re.split('[.!?]\s', text)
print(li2)

# Разделить на слова больше 4-х букв
print('Слова более чем из 4-х букв')
li = re.findall('\w{4,100}', text)
print(li)

print('\nПосчитать первые 10 - количество слов более чем из 4-х букв')
li3 = re.findall('\w{4,100}', text)
print(collections.Counter(li3).most_common(10))

print('\nСсылки в тексте')
pattern = re.compile('[\d]+[\w.]+[/.]+|[\w.]+/\w*[+=?]*\w*[=?]*\d*')
# li5 = re.findall('[\d]+[\w.]+[/.]+|[\w.]+/\w*[+=?]*\w*[=?]*\d*', text)
li5 = pattern.findall(text)
print(li5)

print('\nДоменные имена в тексте')
li4 = re.findall('[\d]+[\w.]+[/.]+|[\w.]+/', text)
print(li4)

print('\nСамое часто упоминаемое доменное имя')
print(collections.Counter(li4).most_common(1))

print('\nЗамена ссылок на \"Ссылка будет доступна после регистрации\"')
new_text = re.sub('[\d]+[\w.]+[/.]+|[\w.]+/\w*[+=?]*\w*[=?]*\d*', '\"Ссылка будет доступна после регистрации\"', text)
print(new_text)
