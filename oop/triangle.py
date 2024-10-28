class Triangolo:
    '''---------------------------------------------
    + base: float
    + altezza: float
    - colore: str
    -----------------------------------------------
    + __init__(base: float, altezza: float) -> None
    + perimetro() -> ...
    + area() -> float
    + set_colore(colore: str) -> None
    + get_colore() -> str
    + cambia_colore(colore: str) -> None
    + get_info() -> str
    -----------------------------------------------'''
    def __init__(self, base: float, altezza: float) -> None:
        self.base = base
        self.altezza = altezza
        self.set_colore('')

    def set_colore(self, colore: str) -> None:
        self.__colore = colore

    def get_colore(self) -> str:
        return self.__colore
    
    def cambia_colore(self, colore) -> None:
        if self.get_colore() == '':
            print('Il colore non è stato mai inizializzato.')
        else:
            self.set_colore(colore)


t = Triangolo(10, 6)
t.cambia_colore('giallorosso')
t.set_colore('biancoceleste')
print(f'Colore: {t.get_colore()}')