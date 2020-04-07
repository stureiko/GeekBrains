import requests
import json


def url_req(url: str):
    req = requests.get(url)
    return req


if __name__ == '__main__':
    appid = 'b6907d289e10d714a6e88b30761fae22'
    service = 'https://samples.openweathermap.org/data/2.5/weather'
    req = url_req(f'{service}?q=London,uk&appid={appid}')
    data = json.loads(req.text)
    print(f"В городе {data[ 'name' ]} {data[ 'main' ][ 'temp' ]} градусов по Кельвину")
