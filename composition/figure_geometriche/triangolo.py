class Triangolo:

    def __init__(self, lato_1: int, lato_2: int, lato_3: int) -> None:
        self.lato_1, self.lato_2, self.lato_3 = lato_1, lato_2, lato_3

    def perimetro(self) -> int:
        return self.lato_1 + self.lato_2 + self.lato_3
    
    def area(self) -> float:
        p = self.perimetro()/2
        return (p * (p-self.lato_1) * (p-self.lato_2) * (p-self.lato_3))**0.5
    