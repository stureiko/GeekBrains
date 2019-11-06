from collections import OrderedDict

a = {'cat': 5, 'mouse': 4, 'dog': 2}

new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(new_a)

new_b = OrderedDict(sorted(a.items(), key=lambda x: x[1]))
print(new_b)

new_b.move_to_end('mouse')
print(new_b)

new_b.move_to_end('mouse', last=False)
print(new_b)

new_b.popitem()
print(new_b)

new_b['cow'] = 2
print(new_b)

new_b['dog'] = 8
print(new_b)

print('*' * 50)

