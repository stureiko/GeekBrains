import re
from bs4 import BeautifulSoup as BS

with open('rbc.html', 'r', encoding='utf-8')as f:
    s = f.read()

soup = BS(s, 'html.parser')
print(soup.prettify())
print(soup.get_text())

print(soup.title.string)

print(soup.div['class'])

li = soup.find_all('a')
for n in li:
    print(n.get('href', ''))



def old_foo():
    global s
    tags = re.compile('<[^<]*>', re.DOTALL)
    script = re.compile('<script.*?</script>', re.DOTALL)
    comments = re.compile('<!--.*?-->')
    s = script.sub('', s)
    s = comments.sub('', s)
    s = tags.sub('', s)
    s = re.sub('[ ]+', ' ', s)
    s = re.sub('\s{2,}', '\n', s)

    print(s)
