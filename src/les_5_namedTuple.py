from collections import namedtuple

hero_1 = ('Aaz', 'Izverd', 100, 0.0, 250)

NewPerson = namedtuple('NewPerson', 'name, race, heath, _mana, strength', rename=True)  # В случае недопустимых имен -
                                                                                        # переименует их само
hero_3 = NewPerson('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_3.race)
print(hero_3)

print('*' * 50)

Point = namedtuple('Point', 'x, y, z')

p1 = Point(2, z=3, y=4)
print(p1)

t = [1, 10, 15]
p2 = Point._make(t)
print(p2)

p3 = p2._replace(x=6)
print(p3)

print(p3._fields)

print('*' * 50)

NewPoint = namedtuple('NewPoint', 'x, y, z', defaults=[0, 0])
p4 = NewPoint(5)
print(p4)
print(p4._fields_defaults)

dct = {'x': 10, 'y': 5, 'z': 20}
p5 = NewPoint(**dct)
print(p5)
