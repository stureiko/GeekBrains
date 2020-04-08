import requests
import json
from pprint import pprint


if __name__ == '__main__':

    service = 'https://api.openweathermap.org/data/2.5/weather'
    appid = '5b7949310b4e93947bded77662051058'

    city = 'Moscow,ru'

    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    params = {'appid': appid,
              'q': city
              }

    res = requests.get(service, headers=headers, params=params)

    if res.ok:
        data = json.loads(res.text)

    print(f"\nВ городе {data[ 'name' ]} сейчас {round(data[ 'main' ][ 'temp' ] - 273.15, 2)} градусов по Цельсию.")

    print('\n')
    print('*'*30)

    pprint(data)
