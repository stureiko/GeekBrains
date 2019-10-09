from player import Player
from hamster import Hamster


hamsters_count = 2

class Game:
    map_width = 6
    map_height = map_width // 2
    map = ''
    for i in range(map_height):
        for j in range(map_width):
            map = map + '*'
        map = map + '\n'
    map = map[:-1]
    game_on = True
    directions = {'w': 's', 's': 'w', 'a': 'd', 'd': 'a'}
    happy_message = 'All Hamsters dead! U-a-o!'

    def __init__(self):
        self.player = Player()
        self.hamsters = []
        for i in range(hamsters_count):
            self.hamsters.append(Hamster(i + 1, self.get_full_map()))

    @staticmethod
    def add_point(position, name, mp):
        li = mp.split("\n")
        row = li[position[1]]
        row = row[:position[0]] + name + row[position[0] + 1:]
        li[position[1]] = row
        return '\n'.join(li)

    def render_map(self):
        s = self.map
        s = self.add_point(self.player.position, 'x', s)
        for h in self.hamsters:
            if h.health > 0:
                s = self.add_point(h.position, str(h.id), s)
        print(s)

    def move_player(self, destination):
        """ destination = a, w, s, d"""
        if destination == 's':
            if self.player.position[1] == len(self.map.split('\n')) - 1:
                return False
            self.player.position[1] += 1
        elif destination == 'a':
            if self.player.position[0] == 0:
                return False
            self.player.position[0] -= 1
        elif destination == 'd':
            #  обработка бага № 1
            if self.player.position[0] == len(self.map.split('\n')[0]) - 1:  # баг 1
                return False
            self.player.position[0] += 1
        elif destination == 'w':
            if self.player.position[1] == 0:
                return False
            self.player.position[1] -= 1
        self.on_move(destination)

    def get_full_map(self):
        s = self.map
        for h in self.hamsters:
            s = self.add_point(h.position, str(h.id), s)
        return s

    def get_hamster_id_on_position(self, coords):
        s = self.get_full_map()
        return s.split('\n')[coords[1]][coords[0]]

    def get_hamster(self, id):
        for h in self.hamsters:
            if h.id == id:
                return h

    def on_move(self, direction):
        # получить позицию хомяка
        hamster_on_field = self.get_hamster_id_on_position(self.player.position)
        if not hamster_on_field == '*':
            self.player.was_hit(int(hamster_on_field))
            if self.player.health <= 0:
                self.game_on = False
                print('Game over, you dead!')
                return False
            print(f'Player: My health: {self.player.health}')
            killed = self.get_hamster(int(hamster_on_field)).on_short()
            if not killed:
                print(f'Hamster: I\'ve been hit! health = {self.get_hamster(int(hamster_on_field)).health} '
                      f'id = {self.get_hamster(int(hamster_on_field)).id}')
                print("Hamster was'n killed")
                self.move_player(self.directions[direction])
            else:  # обработка бага 3
                print(f'Hamster: I\'v been killed, id = {self.get_hamster(int(hamster_on_field)).id}')
                self.hamsters.remove(self.get_hamster(int(hamster_on_field)))
                print(f'Num of Hamsters: {len(self.hamsters)}')
                for h in self.hamsters:
                    print(f'Hamster id = {h.id}')

    def start(self):
        self.render_map()
        while self.game_on:
            if len(self.hamsters) == 0:
                print(self.happy_message)
                break
            command = input("Insert command: ")
            if command in ['a', 's', 'd', 'w']:
                self.move_player(command)
                self.render_map()
            if command == 'exit':
                self.game_on = False
            if command == 'e':
                self.player.wait()


if __name__ == '__main__':
    game = Game()
    game.start()
