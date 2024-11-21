'''
TRACCIA
Aurora ama collezionare e giocare con le macchinine. 
Ogni volta che ne acquista una, la etichetta con una lettera dell’alfabeto 
(continuando dall’ultima posseduta) e la posiziona in coda alle altre, 
su un circuito di forma circolare. 
Una volta posizionate, le macchinine non vengono più rimosse dalla pista. 
Quando gioca, Aurora dà una bella spinta alla macchinina che si trova in prima posizione, 
in modo da farle percorrere l’intero circuito. 
Inizialmente Aurora possiede sei macchinine (A, B, C, D, E, F) ed effettua 10 lanci, 
prima di smettere di giocare per andare a guardare una puntata di Breaking Bad. 
Il giorno seguente Aurora osserva il circuito e trova le macchinine posizionate 
nel seguente ordine: E, F, A, B, C, D (in conseguenza ai lanci del giorno precedente), 
così decide di uscire di casa per acquistare 2 nuove macchinine e posizionarle sul circuito.

Successivamente e nei giorni seguenti, Aurora
- effettua 7 lanci
- acquista 5 nuove macchinine
- effettua 18 lanci
- acquista 1 nuova macchinina.

Scrivi un programma che simuli quanto accaduto sul circuito. 
L’output del programma sarà il posizionamento finale delle macchinine sul circuito, 
es. CDGIJK…ABN.
'''

class Circuito:
    def __init__(self) -> None:
        self.macchine = ['A', 'B', 'C', 'D', 'E', 'F']
        self.ultima = self.macchine[-1]

    def __str__(self) -> str:
        return ''.join(self.macchine)
    
    def acquista(self) -> None:
        nuova_macchina = chr(ord(self.ultima) + 1)
        self.macchine.append(nuova_macchina)
        self.ultima = self.macchine[-1]
    
    def lancio(self) -> None:
        macchina_lanciata = self.macchine.pop(0)
        self.macchine.append(macchina_lanciata)


c = Circuito()
for _ in range(10):
    c.lancio()
c.acquista()
c.acquista()
for _ in range(7):
    c.lancio()
for _ in range(5):
    c.acquista()
for _ in range(18):
    c.lancio()
c.acquista()
print(c)