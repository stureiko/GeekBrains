from random import randint


class Hamster:
    position = [0, 0]
    health: int

    def __init__(self, h_id, map_width, map_height):
        self.id = h_id
        self.health = randint(1, 4)
        self.position = [randint(0, map_width-1), randint(0, map_height-1)]

    def on_short(self):
        self.health -= 1
        print('I have been shorted! id = ' + str(self.id))
