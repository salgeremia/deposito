'''
TRACCIA
Guido è stato rimandato in Informatica. 
Per punizione, i genitori lo obbligano a lavorare tutta l’estate come lavapiatti 
in una nota pizzeria della città. A Guido piace lavare i piatti ed è anche molto veloce 
nel farlo, però ha il difetto di distrarsi spesso (stesso motivo per il quale ha ricevuto 
il debito) e questo fa si che i piatti sporchi si accumulino velocemente. 
I piatti possono essere di tre tipologie: 
per le pizze (P), per i fritti (F) e per i dolci (D). 
Scrivi un programma che simuli quanto accaduto in cucina, sapendo che: 
- ad inizio serata non c’erano piatti da lavare
- dopo un certo periodo di tempo sono arrivati 16 piatti sporchi random (es. P-P-D-F-F-P-P…)
- Guido ne ha lavati 9 e si è concesso una pausa per controllare le notifiche del cellulare
- sono arrivati altri 5 piatti da lavare
- Guido ne ha lavati 8 e si è fermato a chiacchierare con Ciro (il pizzaiolo napoletano)
- sono arrivati gli ultimi 12 piatti da lavare.
Implementa il metodo conta_piatti che consenta a Guido di sapere quanti piatti sporchi 
dovrà lavare prima di (salutare l’amico Ciro e) fare rientro a casa. 
L’output del programma sarà la lista dei piatti lavati, es. DDFPPP…FDPP.

PS: per generare un valore random a partire da una sequenza (lista) puoi importare la libreria 
random e utilizzare la funzione random.choice(lista).
'''
import random

class Lavapiatti:
    def __init__(self) -> None:
        self.piatti_sporchi = list()

    def __str__(self) -> str:
        return f'-> {self.piatti_sporchi}'    

    def aggiungi_piatto(self) -> None:
        tipologia_piatti = ['P', 'F', 'D']
        self.piatti_sporchi.append(random.choice(tipologia_piatti))
    
    def lava_piatto(self) -> None:
        piatto = self.piatti_sporchi.pop()
        print(piatto, end='')

    def conta_piatti(self) -> int:
        return len(self.piatti_sporchi)
    

piatti = Lavapiatti()
print(piatti)
for _ in range(16):
    piatti.aggiungi_piatto()
print(piatti)
for _ in range(9):
    piatti.lava_piatto()
print(piatti)
for _ in range(5):
    piatti.aggiungi_piatto()
print(piatti)
for _ in range(8):
    piatti.lava_piatto()
print(piatti)
for _ in range(12):
    piatti.aggiungi_piatto()
print(piatti)
for _ in range(piatti.conta_piatti()):
    piatti.lava_piatto()
print(piatti)