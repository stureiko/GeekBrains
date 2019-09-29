import requests
from time import sleep

link_s = 'http://127.0.0.1:5000/secret_page?key='
for i in range(70, 90):
    link = link_s+str(i)
    if requests.get(link).text == 'Incorrect key!':
        print('Key: ' + str(i) + ' is incorrect!')
        sleep(1)
        continue
    else:
        print('Key is: ' + str(i))
        break
