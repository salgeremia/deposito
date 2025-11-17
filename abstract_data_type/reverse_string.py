# Esercizio pag. 353 n. 5 - reverse_string

'''
    La classe Pila possiede tre metodi:
    __init__    -> inizializza l'oggetto come lista vuota;
    aggiungi    -> aggiunge un elemento alla fine della lista;
    rimuovi     -> rimuove l'ultimo elemento della lista.
'''
class Pila:
    def __init__(self) -> None:
        self.__pila = list()
    
    def aggiungi(self, elemento: str) -> None:
        self.__pila.append(elemento)

    def rimuovi(self) -> str:
        return self.__pila.pop()


def reverse_string(stringa: str) -> str:
    '''Restituisce la stringa invertita.'''
    stringa_invertita = ''
    pila = Pila()
    for carattere in testo:
        pila.aggiungi(carattere)
    for i in range(len(stringa)):
        stringa_invertita += pila.rimuovi()
    return stringa_invertita


testo = input()
print(reverse_string(testo))