class Pila:
    def __init__(self) -> None:
        self.__pila = list()

    def __str__(self) -> str:
        return str(self.__pila)
    
    def inserisci(self, elemento: int) -> None:
        self.__pila.append(elemento)

    def rimuovi(self) -> None:
        self.__pila.pop()

    def lunghezza(self) -> int:
        return len(self.__pila)
    

p = Pila()
print('Inserisci elementi nella pila (per terminare inserire -1)')
while True:
    elemento = int(input('elemento = '))
    if elemento != -1:
        p.inserisci(elemento)
    else:
        break

da_eliminare = int(input('Quanti elementi vuoi eliminare? '))
if da_eliminare <= p.lunghezza():
    for _ in range(da_eliminare):
        p.rimuovi()

print(p)
