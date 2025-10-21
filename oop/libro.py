'''
Argomento: OOP
Esercizio: Gestione di una biblioteca digitale

Progettare e implementare un piccolo sistema che gestisca libri e audiolibri.

Crea una classe chiamata Libro che abbia i seguenti attributi:
titolo (stringa)
autore (stringa)
anno_pubblicazione (intero)
disponibile (booleano, di default True)

E i seguenti metodi:
__init__(...) per inizializzare gli attributi.
__str__(...) per restituire una stringa descrittiva del libro.
presta() -> imposta disponibile a False e stampa "Il libro è stato prestato."
restituisci() -> imposta disponibile a True e stampa "Il libro è stato restituito."

Crea una sottoclasse di Libro, chiamata Audiolibro, che aggiunga:
un attributo aggiuntivo: durata_minuti (intero)
un metodo ascolta() che stampi qualcosa come:
"Stai ascoltando l’audiolibro <titolo> di <autore> (durata: X minuti)."
Sovrascrivi anche il metodo __str__() in modo che indichi che si tratta di un audiolibro.

Crea un oggetto della classe Libro e uno della classe Audiolibro.
Mostra le informazioni dei libri e audiolibri con print().
Simula:
Il prestito di un libro,
La restituzione di un altro,
L'ascolto di un audiolibro.
'''
class Libro:
    '''
    -----------------------------------------------------------------------------------------------
    - titolo: str
    - autore: str
    - anno_pubblicazione: int
    - disponibile=True: bool
    -----------------------------------------------------------------------------------------------
    - __init__(self, titolo: str, autore: str, anno_pubblicazione: int, disponibile=True) -> None
    - __str__(self) -> str
    + presta(self) -> None
    + restituisci(self) -> None
    + get_titolo(self) -> str
    + get_autore(self) -> str
    -----------------------------------------------------------------------------------------------
    '''
    def __init__(self, titolo: str, autore: str, anno_pubblicazione: int, disponibile=True) -> None:
        self.__titolo = titolo
        self.__autore = autore
        self.__anno_pubblicazione = anno_pubblicazione
        self.__disponibile = disponibile

    def __str__(self) -> str:
        return f'"{self.__titolo}" di {self.__autore} ({self.__anno_pubblicazione}) - Disponibile: {self.__disponibile}'
    
    def presta(self) -> None:
        if self.__disponibile:
            self.__disponibile = False
            print("Il libro è stato prestato.")
        else:
            print("Il libro non è disponibile per il prestito.")
    
    def restituisci(self) -> None:
        if not self.__disponibile:
            self.__disponibile = True
            print("Il libro è stato restituito.")

    def get_titolo(self) -> str:
        return self.__titolo
    
    def get_autore(self) -> str:
        return self.__autore

class Audiolibro(Libro):
    '''
    ------------------------------------------------------------------------------------------------------------------
    - durata_minuti: int
    ------------------------------------------------------------------------------------------------------------------
    - __init__(self, titolo: str, autore: str, anno_pubblicazione: int, durata_minuti: int, disponibile=True) -> None
    - __str__(self) -> str
    + ascolta(self) -> None
    ------------------------------------------------------------------------------------------------------------------
    '''
    def __init__(self, titolo: str, autore: str, anno_pubblicazione: int, durata_minuti: int, disponibile=True) -> None:
        super().__init__(titolo, autore, anno_pubblicazione, disponibile)
        self.__durata_minuti = durata_minuti

    def __str__(self) -> str:
        return f'Audiolibro: {super().__str__()} - Durata: {self.__durata_minuti} minuti'
    
    def ascolta(self) -> None:
        print(f'Stai ascoltando l’audiolibro "{self.get_titolo()}" di {self.get_autore()} (durata: {self.__durata_minuti} minuti).')

# Creazione di un oggetto Libro
l = Libro("1984", "George Orwell", 1949)
print(l)
l.presta()
print(l)
l.restituisci()
print(l)
# Creazione di un oggetto Audiolibro
a = Audiolibro("Il nome della rosa", "Umberto Eco", 1980, 480)
print(a)
a.ascolta()
