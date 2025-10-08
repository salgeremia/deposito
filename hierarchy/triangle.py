class Triangle:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.side_1, self.side_2, self.side_3 = a, b, c

    def __str__(self) -> str:
        return f'> triangle data\nsides:\t1\t2\t3\n\t{self.side_1}\t{self.side_2}\t{self.side_3}'

    def perimeter(self):
        print('perimeter -> class Triangle')
        return self.side_1 + self.side_2 + self.side_3

class EquilateralTriangle(Triangle):
    def __init__(self, side: int) -> None:
        super().__init__(side, side, side)

    def perimeter(self):
        print('perimeter -> class EquilateralTriangle')
        return 3*self.side_1

class IsosceleTriangle(Triangle):
    def __init__(self, oblique_side: int, base: int) -> None:
        super().__init__(oblique_side, oblique_side, base)

    def perimeter(self):
        print('perimeter -> class IsosceleTriangle')
        return 2*self.side_1 + self.side_3


t = Triangle(3, 4, 5)
print(t)
p = t.perimeter()
print('2p =', p)

et = EquilateralTriangle(4)
print(et)
p = et.perimeter()
print('2p =', p)

it = IsosceleTriangle(3, 6)
print(it)
p = it.perimeter()
print('2p =', p)