class Sprite:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f'Hi, I am a {self.name}'

    def distance_to(self, other):
        print(f'{self.name} -> {other.name}')
        return Sprite.distance_between(self, other)
    
    @classmethod
    def distance_between(cls, obj_sprite_1, obj_sprite_2):
        distance_x = obj_sprite_1.x - obj_sprite_2.x
        distance_y = obj_sprite_1.y - obj_sprite_2.y
        distance = (distance_x**2 + distance_y**2)**0.5
        return distance

s1 = Sprite('Dog', 20, 0)
s2 = Sprite('Cat', 60, 30)

d = s1.distance_to(s2)
print(d)

