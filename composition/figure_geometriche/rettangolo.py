class Rettangolo:
    
    def __init__(self, base: int, altezza: int) -> None:
        self.base = base
        self.altezza = altezza
    
    def perimetro(self) -> int:
        return 2 * (self.base + self.altezza)
    
    def area(self) -> int:
        return self.base * self.altezza
    
class Quadrato(Rettangolo):
    
    def __init__(self, lato: int) -> None:
        super().__init__(lato, lato)
    