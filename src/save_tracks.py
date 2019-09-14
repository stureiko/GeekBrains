import json

tracks = [
    {'name': 'Вечная любовь', 'artist': 'Агата кристи'},
    {'name': 'Black', 'artist': 'Bi'}
]

with open('tracks.json', 'w', encoding='utf-8') as f:
    json.dump(tracks, f)

print('Запись завершена')
