# Implemantare una classe per la gestione di rettangoli

class Rettangolo:
    # ATTRIBUTI: base, altezza
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    # METODI: calcolo perimetro, calcolo area, calcolo diagonale
    def perimetro(self):
        return 2 * (self.base + self.altezza)


# Utilizzo della classe
x = Rettangolo(5, 6)
print(x.perimetro())
print(type(x))