class Rectangle:
    # ATTRIBUTES:
    # - width
    # - height
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    # METHODS:
    # - area
    # - perimeter
    # - diagonal
    def area(self) -> int:
        return self.width * self.height
    
    def perimeter(self) -> int:
        return 2 * (self.width + self.height)
    
    def diagonal(self) -> float:
        return (self.width**2 + self.height**2)**0.5


r = Rectangle(6, 8)
print(r.area(), r.perimeter(), r.diagonal())