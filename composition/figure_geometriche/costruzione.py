from triangolo import Triangolo
from rettangolo import Rettangolo, Quadrato
from cerchio import Cerchio

class Costruzione:

    def __init__(self) -> None:
        self.__figure = []

    def aggiungi_figura(self, figura) -> None:
        self.__figure.append(figura)

    def area(self) -> float:
        area_totale = 0.0
        for figura in self.__figure:
            area_totale += figura.area()
        return area_totale
    
    
if __name__ == "__main__":
    costruzione = Costruzione()
    costruzione.aggiungi_figura(Triangolo(3, 4, 5))
    costruzione.aggiungi_figura(Rettangolo(4, 5))
    costruzione.aggiungi_figura(Quadrato(4))
    costruzione.aggiungi_figura(Cerchio(3))
    print("Area totale:", costruzione.area())