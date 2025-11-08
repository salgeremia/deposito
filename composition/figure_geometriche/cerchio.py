class Cerchio:
    
    def __init__(self, raggio: int) -> None:
        self.raggio = raggio
    
    def perimetro(self) -> float:
        return 2 * 3.14 * self.raggio
    
    def area(self) -> float:
        return 3.14 * self.raggio ** 2