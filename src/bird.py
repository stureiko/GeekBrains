class Bird:
    name = 'Unknown'
    distance = 0
    speed = 100
    __step = 1

    def __init__(self, name, speed, steps):
        self.name = name
        self.speed = speed
        for n in range(steps):
            self.run()

    def saw_name(self):
        print(self.name)

    def run(self, distance=False):
        if not distance:
            distance = self.speed
        self.distance += int(distance * (1 + self.__step / 10))
        self.__step += 1


class Chicken(Bird):
    type = 'Chicken'

    def __init__(self, steps):
        super(Chicken, self).__init__('Chicken', 50, steps)
