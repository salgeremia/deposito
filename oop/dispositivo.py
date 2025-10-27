'''
Progettare e realizzare un programma in Python che rappresenti il sistema di gestione 
di dispositivi elettronici, applicando in modo corretto i concetti di incapsulamento, 
ereditarietà e sovrascrittura di metodi.

Consegna

1. Definizione delle classi

Implementare due classi:
- classe base chiamata Dispositivo
- sottoclasse chiamata Smartphone, che eredita da Dispositivo

2. Classe Dispositivo

Definisci la classe Dispositivo con le seguenti caratteristiche:

Attributi: 
codice_seriale, marca, modello e prezzo. 
Il codice seriale è un attributo privato, mentre gli altri sono pubblici. 
Gli attributi sono tutti di tipo testuale, eccetto il prezzo che è di tipo decimale.

Metodi:
inizializzatore che inizializza tutti gli attributi;
setter e getter per modificare e per restituire il valore dell’attributo privato;
descrizione per restituire una stringa formattata con le informazioni principali del dispositivo 
(es. "Dispositivo di marca X, modello Y: prezzo € 600.00);
sconto per calcolare e restituire il prezzo scontato del dispositivo in base alla percentuale 
ricevuta come parametro.

3. Classe Smartphone (sottoclasse di Dispositivo)

Definisci la classe Smartphone che eredita da Dispositivo e aggiunge nuove caratteristiche.

Attributi aggiuntivi:
memoria, espressa in GB (es. 128, 256, 512, ecc.), e sistema operativo (es. Android, Apple, ecc.).
Metodi:
inizializzatore che richiama quello della superclasse;
setter e getter per modificare e per restituire il valore dell’attributo privato "memoria_gb";
descrizione che sovrascrive il metodo della superclasse, aggiungendo informazioni relative a memoria 
e sistema operativo dello Smartphone;
top_di_gamma che restituisce vero se il prezzo è superiore a 800 euro e la memoria è almeno 128 GB, 
altrimenti restituisce falso.

4. Esempio di utilizzo

- Istanzia un oggetto Dispositivo e un oggetto Smartphone;
- Stampa le descrizioni di entrambi utilizzando il metodo;
- Applica e mostra un esempio di sconto a entrambi;
- Modifica e ristampa il codice seriale del dispositivo e la memoria dello smartphone;
- Stampa a video un messaggio per indicare se lo smartphone è top di gamma.

5. Diagramma UML

Disegna il diagramma UML delle due classi, facendo attenzione ad indicare la visibilità degli attributi 
e dei metodi, i tipi di dati (per attributi e parametri) e i valori di ritorno dei metodi.
'''

class Dispositivo:
    '''
    ---
    - codice_seriale: str
    + marca: str
    + modello: str
    + prezzo: float
    ---
    - __init__(codice_seriale: str, marca: str, modello: str, prezzo: float) -> None
    + set_codice_seriale(codice_seriale: str) -> None
    + get_codice_seriale() -> str
    + descrizione() -> str
    + sconto(percentuale: float) -> float
    ---
    '''
    def __init__(self, codice_seriale: str, marca: str, modello: str, prezzo: float) -> None:
        self.__codice_seriale = codice_seriale
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo

    def set_codice_seriale(self, codice_seriale: str) -> None:
        self.__codice_seriale = codice_seriale
    
    def get_codice_seriale(self) -> str:
        return self.__codice_seriale
    
    def descrizione(self) -> str:
        return f'Dispositivo di marca {self.marca}, modello {self.modello}: prezzo € {self.prezzo:.2f}'
    
    def sconto(self, percentuale: float) -> float:
        return self.prezzo * (1 - percentuale / 100)

class Smartphone(Dispositivo):
    '''
    ---
    - memoria_gb: int
    + sistema_operativo: str
    ---
    - __init__(codice_seriale: str, marca: str, modello: str, prezzo: float, memoria_gb: int, sistema_operativo: str) -> None
    + set_memoria_gb(memoria_gb: int) -> None
    + get_memoria_gb() -> int
    + descrizione() -> str
    + top_di_gamma() -> bool
    ---
    '''
    def __init__(self, codice_seriale: str, marca: str, modello: str, prezzo: float, memoria_gb: int, sistema_operativo: str) -> None:
        super().__init__(codice_seriale, marca, modello, prezzo)
        self.__memoria_gb = memoria_gb
        self.sistema_operativo = sistema_operativo

    def set_memoria_gb(self, memoria_gb: int) -> None:
        self.__memoria_gb = memoria_gb
    
    def get_memoria_gb(self) -> int:
        return self.__memoria_gb
    
    def descrizione(self) -> str:
        base_desc = super().descrizione()
        return f'{base_desc}, memoria: {self.__memoria_gb} GB, sistema operativo: {self.sistema_operativo}'
    
    def top_di_gamma(self) -> bool:
        return self.prezzo > 800 and self.__memoria_gb >= 128
    

# Esempio di utilizzo
if __name__ == "__main__":
    d = Dispositivo('abc012', 'X', 'Y', 750)
    s = Smartphone('def345', 'W', 'Z', 850, 256, 'K')
    print(f'{d.descrizione()}\n{s.descrizione()}')
    sconto = 15
    print(f'Prezzo dispositivo dopo sconto: € {d.sconto(sconto):.2f}')
    print(f'Prezzo smartphone dopo sconto: € {s.sconto(sconto):.2f}')
    d.set_codice_seriale('ghi789')
    print(f'Nuovo codice seriale dispositivo: {d.get_codice_seriale()}')
    print(f'Memoria smartphone: {s.get_memoria_gb()} GB')
    print(f'Smartphone è top di gamma: {s.top_di_gamma()}')
