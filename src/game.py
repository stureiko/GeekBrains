from player import Player
from hamster import Hamster

hamsters_count = 4


class Game:
    map = """********\n********\n********\n********"""

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
            if self.player.position[1] == len(self.map.split('\n')[0]) - 1:
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

    def get_hamster_on_position(self, coords):
        s = self.get_full_map()
        return s.split('\n')[coords[1]][coords[0]]

    directions = {'w': 's', 's': 'w', 'a': 'd', 'd': 'a'}

    def on_move(self, direction):
        hamster_on_field = self.get_hamster_on_position(self.player.position)
        if not hamster_on_field == '*':
            killed = self.hamsters[int(hamster_on_field)-1].on_short()
            if not killed:
                print(f'I have been shorted! health = {self.hamsters[int(hamster_on_field)-1].health} '
                      f'id = {self.hamsters[int(hamster_on_field)-1].id}')
                print("was'n killed")
                self.move_player(self.directions[direction])
            else:
                print(f'I have been killed, id = {self.hamsters[int(hamster_on_field)-1].id}')

    def start(self):
        self.render_map()
        while True:
            command = input("Insert command: ")
            if command in ['a', 's', 'd', 'w']:
                self.move_player(command)
                self.render_map()
            if command == 'exit':
                break


if __name__ == '__main__':
    game = Game()
    game.start()
