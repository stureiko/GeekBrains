import re

with open('rbc.html', 'r', encoding='utf-8')as f:
    s = f.read()

tags = re.compile('<[^<]*>', re.DOTALL)
script = re.compile('<script.*?</script>', re.DOTALL)
comments = re.compile('<!--.*?-->')
s = script.sub('', s)
s = comments.sub('', s)
s = tags.sub('', s)
s = re.sub('[ ]+', ' ', s)
s = re.sub('\s{2,}', '\n', s)

print(s)
