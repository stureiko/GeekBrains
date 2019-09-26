import re
from bs4 import BeautifulSoup as BS

try:
    with open('geekbrains.html', 'r', encoding='utf-8') as f:
        text = f.read()
except FileNotFoundError:
    text = ''

print('=========== через библиотеку re ===========\n')

num_students = re.compile('<span class="total-users">Нас уже ([\d\s]+) человек</span>')
li = num_students.findall(text)
# print(li)
s = ' '.join(li)
print(s)
s = ''

print('=========== через библиотеку BeautifulSoup ===========\n')
sp = BS(text, 'html.parser')
li2 = sp.find_all('span')
s = [s.get_text() for s in li2 if s.get('class', '') == ['total-users']]

# print(li2)
print(s)
s = ' '.join(s)
s = [a for a in s.split() if a.isdigit()]
s = ' '.join(s)

print(s)
