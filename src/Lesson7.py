# Тернарный оператор
# результат 1 если условие иначе результат 2
print('Возвращаем истину')
condition = True
print('Max' if condition else 'Min')

print('Возвращаем ложь')
condition = False
print('Max' if condition else 'Min')

# слово -> СлОвО
word = 'слово'
result = []

for i in range(len(word)):
    letter = word[i]
    letter = letter.lower() if i % 2 != 0 else letter.upper()
    result.append(letter)

result = ''.join(result)
print(result)

# ввод пароля

