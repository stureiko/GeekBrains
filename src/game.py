import os
from player import Player


class Game:
    map = """********\n********\n********\n********"""

    def __init__(self):
        self.player = Player()

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

    def start(self):
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
