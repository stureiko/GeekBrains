import requests
from bs4 import BeautifulSoup as BS

url = 'http://www.yandex.ru'
html = requests.get(url)
print(html)

soup = BS(html.text, 'html.parser')

li = soup.find_all('div')

li1 = [s.get_text() for s in li if s.get('class') == ['weather__temp']]
weather = ' '.join(li1)
print(weather)

li2 = soup.findAll('div', {'class': 'weather__icon'})[0]
li2 = li2.get('title')
print(li2)

li_temp = [s.get_text() for s in li if s.get('class') == ['weather__forecast']]
li_temp = ' '.join(li_temp)
print(li_temp)

li3 = [s.get_text() for s in li if s.get('class') == ['traffic__rate-text']]
traffic = ' '.join(li3)

traf_for = [s.get_text() for s in li if s.get('class') == ['traffic__forecast']]
traf_for = ' '.join(traf_for)

print(traffic + ' баллов - ' + traf_for)
