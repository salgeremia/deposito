class Sprite:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f'Hi, I am a {self.name}'

    def distance_to(self, other):
        print(f'{self.name} -> {other.name}')


s1 = Sprite('Dog', 20, 0)
s2 = Sprite('Cat', 60, 0)
s1.distance_to(s2)
print(s1)