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
# Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)

# Теперь надо добавить новую функцию, которая будет вычислять и
# возвращать полученный урон по формуле damage / armor

# Следовательно, у вас должно быть 2 функции:

# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.

# Примечание. Функция номер 2 используется внутри функции номер 1
# для вычисления урона и вычитания его из здоровья персонажа.



def input_attr(atr_name: str, type_of_value):
    """
    Ввод атрибута игрока - здоровье, урон или защита
    # второй парамет - тип зачения на которое проверяется вводимый параметр
    # в данном контексте int или float
    :param atr_name: имя атрибута
    :param type_of_value: тип значения
    :return: значение атрибута
    """
    while True:
        atr = input(f'Введите значение {atr_name}: ')
        try:
            atr = type_of_value(atr)
            break
        except ValueError:
            print('Значение должно типом {}'.format(type_of_value))
    return atr


def print_player_atr(player: dict):
    """
    Печать атрибутов игрока
    :param player: игрок
    :return: None
    """
    print('Игрок: {}, здоровье {}, атака {}, защита {}'.format(player['name'], player['health'], player['damage'],
                                                                 player['armor']))


players = []


player1 = {'name': input('Введите имя игрока 1: '),
           'health': input_attr('health', int),
           'damage': input_attr('damage', int),
           'armor': input_attr('armor', float)}

player2 = {'name': input('Введите имя игрока 2: '),
           'health': input_attr('health', int),
           'damage': input_attr('damage', int),
           'armor': input_attr('armor', float)}

players.append(player1)
players.append(player2)

# Выводим игроков
print('\nИгроки:')
for player in players:
    print_player_atr(player)


def attack(player_attack: dict, player_defense: dict):
    """
    Функция атаки
    :param player_attack: атакующий игрок
    :param player_defense: атакуемый игрок
    :return: возвращает значение здоровья у атакуемого
    """
    print('\nИгрок {} атакует игрока {}'.format(player_attack['name'], player_defense['name']))
    player_defense['health'] = int(player_defense['health'] - get_damage(player_attack['damage'], player_defense['armor']))
    return player_defense['health']


def get_damage(damage: int, armor: float):
    """
    Вычисляет величину урона от атаки с учетом защиты
    :param damage: урон атакующего
    :param armor: защита атакуемого
    :return: величина снижения здоровья атакуемого
    """
    return damage/armor


attack(player1, player2)

# Вывести игроков после боя
print('\nИгроки после боя:')
for player in players:
    print_player_atr(player)
