from collections import deque
import random

a = deque()
b = deque('abcdef')
c = deque([1, 2, 3, 4, 5])

print(a, b, c, sep='\n')

print('*'*50+'\n')
d = deque([i for i in range(5)], maxlen=7)
print(d)
d.append(5)  # добавить элемент в конец
print(d)
d.appendleft(6)  # добавить элемент в начало
print(d)
d.extend([7, 8, 9])  # добавляем несколько элементов
d.extendleft([10, 11, 12])  # добавляем элементы слева
print(d)

print('*'*50+'\n')
f = deque([i for i in range(5)], maxlen=7)
print(f)
x = f.pop()
y = f.popleft()
print(f, x, y, sep='\n')
print(len(f))
print(list(f))

print('*'*50+'\n')


array = [random.randint(-100, 100) for _ in range(10)]
print(array)

deq = deque()

for item in array:
    if item >= 0:
        deq.append(item)
    if item < 0:
        deq.appendleft(item)

print(deq)


