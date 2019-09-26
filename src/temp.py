import re

with open('yandex_source.html', 'r', encoding='utf-8') as f:
    text = f.read()

li = re.findall('aria-label\=\"([\w+\s]*[\+\-]\d{1,2}\s°C[\s,\w+]*)', text)
print(li)

li1 = re.findall('aria-label\=\"[\w+\s]*([\+\-]\d{1,2})\s°C[\s,\w+]*', text)
print(li1)
