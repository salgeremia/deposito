class Retta:
    def __init__(self, m, q) -> None:
        self.m = m
        self.q = q

    def __str__(self) -> str:
        if self.q < 0:
            return f'y = {self.m}x{self.q}'    
        return f'y = {self.m}x+{self.q}'

    def appartiene(self, x, y) -> bool:
        if y == self.m * x + self.q:
            return True
        return False


m = int(input('m = '))
q = int(input('q = '))
r = Retta(m, q)
print(r)
print(r.appartiene(1, 4))
print(r.appartiene(1, 5))