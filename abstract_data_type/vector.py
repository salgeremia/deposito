class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y
    
    def module(self) -> float:
        return (self.x**2 + self.y**2)**0.5
    
    def sum(self, other: Vector) -> Vector:
        x_s = self.x + other.x
        y_s = self.y + other.y
        return Vector(x_s, y_s)
    
    def __str__(self) -> str:
        return f'> vector({self.x}; {self.y}) => |{self.module():.2f}|'
    

v = Vector(3, 4)
print(v)
w = Vector(6, 2)
print(w)
s = v.sum(w)
print(s)
