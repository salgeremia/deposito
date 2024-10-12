'''
ESERCIZIO pag. 309 n. 4
Leggendo tutti i commenti inseriti con il cancelletto (#) 
è possibile ricostruire l'intera traccia dell'esercizio.
Altri commenti, inseriti con gli apici, facilitano la 
comprensione del codice e spiegano le scelte implementative.
'''

# Definisci la classe Television, per rappresentare televisori
class Television:
    # caratterizzati dai seguenti attributi:
    # il canale corrente compreso tra 1 e 999;
    # il volume corrente compreso tra 0 e 100;
    # lo stato acceso (True) e spento (False).

    # Definisci il metodo costruttore per inizializzare lo stato del televisore.
    def __init__(self, state: bool) -> None:
        '''Inizializza lo stato del televisore.'''
        self.set_state(state)
        '''Gli altri attributi assumono valori di default.'''
        self.__channel = 1
        self.__volume = 0

    # Applica l'incapsulamento, nascondendo gli attributi e aggiungendo i metodi getter e setter
    # per ottenere e modificare ciascun attributi, verificando che i valori impostati dai metodi
    # setter siano corretti.
    ''' - - - - - - - - - - - - - - - - - - METODI SETTER - - - - - - - - - - - - - - - - - - '''
    def set_state(self, state: bool) -> None:
        '''Setta lo stato del televisore.'''
        self.__state = state

    # Il canale successivo del canale successivo del canale 999 è il canale 1
    # e il 999 è il canale precedente del canale 1.
    def set_channel(self, channel: int) -> None:
        '''Setta il canale del televisore, verificando che sia compreso tra 1 e 999.'''
        if channel == 0:
            self.__channel = 999
        elif channel == 1000:
            self.__channel = 0
        else:
            self.__channel = channel

    # Incrementare il volume oltre il valore 100, o decrementare il volume sotto il valore 0,
    # non deve produrre effetti, né sollevare eccezioni.
    def set_volume(self, volume: int) -> None:
        '''Setta il volume del televisore, verificando che sia compreso tra 0 e 100.'''
        if 0 <= volume <= 100:
            self.__volume = volume
        '''Se la condizione è falsa non deve succedere niente, quindi l'else è da evitare.'''
    
    ''' - - - - - - - - - - - - - - - - - - METODI GETTER - - - - - - - - - - - - - - - - - - '''
    def get_state(self) -> bool:
        '''Restituisce lo stato del televisore.'''
        return self.__state
    
    def get_channel(self) -> int:
        '''Restituisce il canale del televisore.'''
        return self.__channel
    
    def get_volume(self) -> int:
        '''Restituisce il volume del televisore.'''
        return self.__volume
    ''' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - '''
    # Aggiungi, inoltre i metodi next_channel() e prev_channel(), per passare al canale
    # precedente/successivo...
    def next_channel(self) -> None:
        '''Cambia il canale con il successivo.'''
        self.set_channel(self.__channel + 1)

    def prev_channel(self) -> None:
        '''Cambia il canale con il precedente.'''
        self.set_channel(self.__channel - 1)

    # ...i metodi volume_up() e volume_down(), per aumentare o diminuire di un fattore 1.
    def volume_up(self) -> None:
        '''Aumenta il volume.'''
        self.set_volume(self.__volume + 1)

    def volume_down(self) -> None:
        '''Diminuisce il volume.'''
        self.set_volume(self.__volume - 1)

    '''Implemento il metodo __str__() per migliorare la leggibilità di ciò che accade all'oggetto.'''
    def __str__(self) -> str:
        if self.__state == True:
            return f'La televisione è ACCESA sul canale {self.__channel} con volume {self.__volume}.'
        else:
            return 'La televisione è SPENTA.'


'''Esempio di utilizzo della classe Television.'''
t = Television(True)

'''Vado al canale 7...'''
t.set_channel(7)
'''...e alzo il volume.'''
for _ in range(20):
    t.volume_up()
print(t)

'''Vado avanti di due canali.'''
t.next_channel()
t.next_channel()
print(t)

'''Spengo la tv.'''
t.set_state(False)
print(t)

'''Riaccendo la tv.'''
t.set_state(True)
print(t)