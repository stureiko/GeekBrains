from random import randint, choice


class Hamster:
    position = [0, 0]
    health: int

    def __init__(self, h_id, map: str):
        self.id = h_id
        self.health = randint(1, 4)
        self.position = self.get_clear_position(map)

    @staticmethod
    def get_clear_position(map: str):
        map_height = len(map.split('\n'))
        map_width = len(map.split('\n')[0])
        while True:
            coords = [randint(0, map_width - 1), randint(0, map_height - 1)]
            if map.split('\n')[coords[1]][coords[0]] == '*':
                return coords

    def on_short(self):
        self.health -= 1
        return self.health == 0
