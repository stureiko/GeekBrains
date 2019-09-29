import requests
import json

link = "https://samples.openweathermap.org/data/2.5/weather?q=Moscow,ru&appid=b6907d289e10d714a6e88b30761fae22"

html = requests.get(link)
text = html.text
data = json.loads(text)
print(data['main']['temp'])
