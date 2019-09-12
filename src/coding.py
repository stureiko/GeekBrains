# Работа с кодировками строк
# типы данных строк:
# str - обычная строка
# byte - строка байт
# bytearray - изменяемая строка байт

s = 'Hello world'
print(type(s))

sb = b'Hello World'
print(type(sb))
print(sb)

# Индексы
print('\nИндексы')
print(s[1])   # получаем символ
print(sb[1])  # получаем код символа

# Срезы
print('\nСрезы')
print(s[1:3])
print(sb[1:3])

# При переборе - получим набор кодов символов строки
print('\nПеребор символов')
for i in sb:
    print(i)

# Перевод строки в байты
print('\nПеревод строки в байты')
sb = 'Hello World Мир'.encode('utf-8')
print(sb[1])
print(sb)

# Перевод байт в строку
print('\nПеревод байт в строку')
s = sb.decode('utf-8')
print(s)
