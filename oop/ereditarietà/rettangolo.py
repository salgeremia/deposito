class Rettangolo:
    def __init__(self, base: int, altezza: int) -> None:
        self.__base, self.__altezza = base, altezza

    def area(self) -> int:
        return self.__base * self.__altezza

    def get_base(self) -> int:
        return self.__base

    def get_altezza(self) -> int:
        return self.__altezza
    

class Parallelepipedo(Rettangolo):
    def __init__(self, base: int, altezza:int, profondità: int) -> None:
        super().__init__(base, altezza)
        self.__profondità = profondità

    def area(self) -> int:
        b, h = super().get_base(), super().get_altezza()
        return 2 * (b * h + self.__profondità * (b + h))


r = Rettangolo(5, 3)
p = Parallelepipedo(4, 5, 2)

print(r.area())
print(p.area())
