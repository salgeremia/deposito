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

    # Definisci il metodo inizializzatore per inizializzare lo stato del televisore.
    def __init__(self, state: bool, channel: int, volume: int) -> None:
        '''Inizializza lo stato del televisore.'''
        # self.set_state(state)
        self.__state = state
        self.__channel = self.set_channel(channel)
        self.__volume = self.set_volume(volume)
        '''Gli altri attributi assumono valori di default.'''
        # self.__channel = 1
        # self.__volume = 0

    # Applica l'incapsulamento, nascondendo gli attributi e aggiungendo i metodi getter e setter
    # per ottenere e modificare ciascun attributo, verificando che i valori impostati dai metodi
    # setter siano corretti.
    ''' - - - - - - - - - - - - - - - - - - METODI SETTER - - - - - - - - - - - - - - - - - - '''

    # Il canale successivo del canale 999 è il canale 1
    # e il 999 è il canale precedente del canale 1.
    def set_channel(self, channel: int) -> None:
        if 1 <= channel <= 999:
            self.__channel = channel
        else:
            self.__channel = 1

    # Incrementare il volume oltre il valore 100, o decrementare il volume sotto il valore 0,
    # non deve produrre effetti, né sollevare eccezioni.
    def set_volume(self, volume: int) -> None:
        if 0 <= volume <= 100:
            self.__volume = volume
        else:
            self.__volume = 0
    
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
        if self.__channel == 999:
            self.__channel = 1
        else:
            self.__channel += 1

    def prev_channel(self) -> None:
        '''Cambia il canale con il precedente.'''
        if self.__channel == 1:
            self.__channel = 999
        else:
            self.__channel -= 1

    # ...i metodi volume_up() e volume_down(), per aumentare o diminuire di un fattore 1.
    def volume_up(self) -> None:
        '''Aumenta il volume.'''
        if self.__volume < 100:
            self.__volume += 1

    def volume_down(self) -> None:
        '''Diminuisce il volume.'''
        if self.__volume > 0:
            self.__volume -= 1

    '''Implemento il metodo __str__() per migliorare la leggibilità di ciò che accade all'oggetto.'''
    def __str__(self) -> str:
        if self.__state == True:
            return f'La televisione è ACCESA sul canale {self.__channel} con volume {self.__volume}.'
        else:
            return 'La televisione è SPENTA.'


'''Esempio di utilizzo della classe Television.'''
t = Television(True, 1250, 300)
print(t)
