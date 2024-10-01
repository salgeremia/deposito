# RISORSE UTILI:
# https://realpython.com/python3-object-oriented-programming/

class Rettangolo:

    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)
    
    def area(self):
        return self.base * self.altezza
    
    def diagonale(self):
        return (self.base**2 + self.altezza**2)**0.5


r = Rettangolo(4, 3)
print(r.perimetro(), r.area(), r.diagonale())