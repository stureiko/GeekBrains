input_str = 'hello'

symbols = {}
# посчитат количество входжений символа в строку
for s in set(input_str):
    print(f'\'{s}\': {input_str.count(s)}')
    symbols[s] = input_str.count(s)

print('*' * 50)
# print(symbols, sep='\n')

# отсортируем по убыванию частоты вхождения
list_d = list(symbols.items())
list_d.sort(key=lambda i: -i[1])
print(*list_d, sep='\n')

# построить дерево Хаффмана

