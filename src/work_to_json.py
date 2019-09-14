import json

friends = [
    {'Name': 'Опа', 'age': 23, 'phones': [123, 345]},
    {'Name': 'Leo', 'age': 35}
]

print(type(friends))
print(friends)

# Преодрабование объекта в строку json
json_friends = json.dumps(friends)

print(type(json_friends))
print(json_friends)

# Обратное преобразование из строки json в объект
friends = json.loads(json_friends)
print(type(friends))
print(friends)
