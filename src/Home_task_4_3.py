# 3: Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
#
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои.
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и
# отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

name = input('Введите имя игрока 1: ')

player1 = {'name': name, 'health': 150, 'damage': 100}
name = input('Введите имя игрока 2: ')
player2 = {'name': name, 'health': 150, 'damage': 100}

print('Игроки:')
print('Игрок 1 {}, здоровье {}, атака {}'.format(player1['name'], player1['health'], player1['damage']))
print('Игрок 2 {}, здоровье {}, атака {}'.format(player2['name'], player2['health'], player2['damage']))


def attack(player_attack: dict, player_defense: dict):
    player_defense['health'] = player_defense['health'] - player_attack['damage']
    return player_defense['health']


attack(player1, player2)

print('\nИгроки после боя:')
print('Игрок 1 {}, здоровье {}, атака {}'.format(player1['name'], player1['health'], player1['damage']))
print('Игрок 2 {}, здоровье {}, атака {}'.format(player2['name'], player2['health'], player2['damage']))
