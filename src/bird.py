class Bird:
    name = 'Unknown'
    distance = 0
    speed = 100

    def __init__(self, name, distance, speed):
        self.name = name
        self.distance = distance
        self.speed = speed

    def saw_name(self):
        print(self.name)

    def run(self, distance=speed):
        self.distance += distance


owl = Bird('Owl', 200, 100)


eagle = Bird('Eagle', 100, 300)

owl.saw_name()
eagle.saw_name()

print(owl.distance)
owl.run(200)
print(owl.distance)
owl.run()
print(owl.distance)
