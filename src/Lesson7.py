import random

# Тернарный оператор
# результат 1 если условие иначе результат 2
print('\n*************** Тернарный оператор ****************')
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

# **************** Генераторы **********************
print('\n*************** Генераторы ****************')
numbers = [1, 2, 3, 4, 5, -1, -2, -3]
result = [number for number in numbers if number > 0]
print(result)

# список из 10 случайных чисел
numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

# списко квадратов чисел из списка
numbers = [-2, 4, 2, 9, 4, 5]
squares = [number**2 for number in numbers]
print(squares)

# имена на букву 'А' из списка
names = ['Андрей', 'Борис', 'Алексей', 'Денис']
a_names = [name for name in names if name.startswith('А')]
print(a_names)
