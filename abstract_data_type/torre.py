'''
Il piccolo Michele, detto Lele, adora gli oggetti colorati e ama impilare tutto ciò che ha una forma circolare. 
Ogni giorno si diverte a costruire una piccola torre nel salotto di casa dei nonni, disponendo i dischi colorati 
uno sopra l’altro in modo da conservare sempre una forma piramidale: i dischi più grandi in basso, quelli più piccoli 
in alto (vedi immagine "Torre di Lele").

Lele però non è ancora molto ordinato: aggiunge dischi, poi cambia idea, ne rimuove alcuni, ne aggiunge altri e 
continua così finché non è soddisfatto del risultato.

Individua la struttura dati astratta che meglio consenta di modellare il comportamento della torre di dischi e 
implementa un codice che soddisfi i seguenti requisiti:
- deve essere possibile aggiungere un nuovo disco alla torre solo se la sua dimensione è minore o uguale a quella del 
disco attualmente in cima;
- deve essere possibile rimuovere, uno alla volta, i dischi situati più in alto;
- la struttura deve garantire in ogni momento la forma piramidale della torre.
'''

class Torre:
    def __init__(self) -> None:
        self.torre = list()

    def stampa(self) -> None:
        print('TORRE:')
        for disco in self.torre[::-1]:
            print(f'|{disco}|')
        print(' -')

    def aggiungi(self, disco: int) -> None:
        # se la torre è vuota
        if not self.torre: 
            self.torre.append(disco)
        else:
            # se l'ultimo disco presente è maggiore del disco che voglio inserire
            if self.torre[-1] > disco:
                self.torre.append(disco)

    def rimuovi(self) -> None:
        if self.torre:
            disco = self.torre.pop()

    # metodo non richiesto dalla traccia
    def svuota(self) -> None:
        while self.torre:
            self.rimuovi()
        
if __name__ == "__main__":
    torre = Torre()
    for i in range(9, 0, -1):
        torre.aggiungi(i)
    torre.svuota()
    torre.stampa()
    torre.aggiungi(3)
    torre.aggiungi(5)
    torre.aggiungi(1)
    torre.stampa()