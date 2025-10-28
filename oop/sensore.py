'''
Progettare e implementare un programma in Python che rappresenti un semplice sistema 
di gestione di sensori ambientali, applicando correttamente i principi della 
programmazione orientata agli oggetti: incapsulamento (attributi pubblici e privati), 
ereditarietà, sovrascrittura di metodi, operazioni e calcoli nei metodi di classe.

1. Definizione delle classi

Implementa due classi:
una classe base chiamata "Sensore";
una sottoclasse chiamata "SensoreTemperatura", che eredita da "Sensore".

2. Classe "Sensore"

Definisci la classe con le seguenti caratteristiche:

Attributi:
id_sensore, posizione, unità_misura e letture. L’id è un codice alfanumerico (es. xyz001) 
ed è l’unico attributo privato, la posizione e l’unità di misura (Celsius o "c" di default) 
sono stringhe, l’attributo letture rappresenta una lista di valori numerici 
(es. 34.5, 32.0, 36.9).

Metodi:
inizializzatore che inizializza tutti gli attributi;
setter e getter per impostare un nuovo valore dell’ID del sensore e per farselo restituire;
aggiungi_lettura per aggiungere una nuova lettura alla lista delle letture;
media_letture per restituire la media aritmetica delle letture registrate (restituisce 0 
se la lista è vuota);
descrizione per restituire una stringa contenente ID, posizione e numero totale di letture.

3. Classe "SensoreTemperatura"

Definisci la classe che eredita da "Sensore" e aggiunge le seguenti caratteristiche.

Attributi:
limite_allarme e stato_allarme, dove il primo attributo è privato e indica il valore limite 
raggiungibile dalla temperatura (es. 39,9), mentre il secondo attributo è pubblico ed è true 
se l’ultima lettura supera il limite, altrimenti false.

Metodi:
inizializzatore che richiama quello della superclasse e imposta il limite di allarme e lo stato 
iniziale dell’allarme (False di default);
setter e getter per impostare un nuovo limite di allarme e per farselo restituire;
aggiorna_stato per impostare lo stato_allarme = True se l’ultima lettura supera il limite, 
altrimenti False;
descrizione che sovrascrive il metodo della superclasse, per aggiungere unità di misura, valore 
medio e stato dell’allarme.

Metodo bonus (FACOLTATIVO):
scostamento_medio per restituire la differenza assoluta media tra ciascuna lettura e la media 
complessiva (indice di variabilità). 
Lo scostamento medio è una misura statistica della variabilità che indica la distanza media dei 
dati da un valore centrale, come la media aritmetica. 
Si calcola come la media dei valori assoluti delle differenze tra ogni dato e la media del set 
di dati.

4. Esempio di utilizzo

- Istanzia un oggetto Sensore e un oggetto SensoreTemperatura, ciascuno con alcune letture 
iniziali.
- Visualizza le descrizioni di entrambi i sensori.
- Aggiungi due nuove letture per il sensore di temperatura: la prima minore del valore limite 
e la seconda superiore.
- Del sensore di temperatura, mostra: la media delle letture e il risultato del metodo 
descrizione.

5. Diagramma UML

Disegna il diagramma UML delle due classi, facendo attenzione ad indicare la visibilità degli 
attributi e dei metodi, i tipi di dati (per attributi e parametri) e i valori di ritorno dei 
metodi.
'''
from typing import Optional

class Sensore:
    '''
    ---
    - id_sensore: str
    + posizione: str
    + unità_misura: str
    + letture: list[float]
    ---
    - __init__(id_sensore: str, posizione: str, letture: list[float] | None = None, unità_misura: str = "C") -> None
    + set_id_sensore(id_sensore: str) -> None
    + get_id_sensore() -> str
    + aggiungi_lettura(lettura: float) -> None
    + media_letture() -> float
    + descrizione() -> str
    '''

    def __init__(self, id_sensore: str, posizione: str, letture: list[float], unità_misura: str = "C") -> None:
        self.__id_sensore = id_sensore
        self.posizione = posizione
        self.unità_misura = unità_misura
        self.letture = letture if letture is not None else []

    def set_id_sensore(self, id_sensore: str) -> None:
        self.__id_sensore = id_sensore
    
    def get_id_sensore(self) -> str:
        return self.__id_sensore
    
    def aggiungi_lettura(self, lettura: float) -> None:
        self.letture.append(lettura)

    def media_letture(self) -> float:
        if not self.letture:
            return 0.0
        return sum(self.letture) / len(self.letture)
    
    def descrizione(self) -> str:
        return (
            f'\nDati sensore:\n'
            f'> id\t\t{self.__id_sensore}\n'
            f'> posizione\t{self.posizione}\n'
            f'> n° letture\t{len(self.letture)}'
        )

class SensoreTemperatura(Sensore):
    '''
    ---
    - limite_allarme: float
    + stato_allarme: bool
    ---
    - __init__(id_sensore: str, posizione: str, letture: list[float], limite_allarme: float, unità_misura: str = "C") -> None
    + set_limite_allarme(limite: float) -> None
    + get_limite_allarme() -> float
    + aggiorna_stato() -> None
    + descrizione() -> str
    + scostamento_medio() -> float
    ---
    '''

    def __init__(self, id_sensore: str, posizione: str, letture: list[float], limite_allarme: float, unità_misura: str = "C") -> None:
        super().__init__(id_sensore, posizione, letture, unità_misura)
        self.__limite_allarme = limite_allarme
        self.aggiorna_stato()

    def set_limite_allarme(self, limite: float) -> None:
        self.__limite_allarme = limite
        self.aggiorna_stato()

    def get_limite_allarme(self) -> float:
        return self.__limite_allarme

    def aggiorna_stato(self) -> None:
        if not self.letture:
            self.stato_allarme = False
        else:
            self.stato_allarme = self.letture[-1] > self.__limite_allarme

    def aggiungi_lettura(self, lettura: float) -> None:
        super().aggiungi_lettura(lettura)
        self.aggiorna_stato()

    def descrizione(self) -> str:
        base = super().descrizione()
        media = self.media_letture()
        return (
            f'{base}\n'
            f'> unità_misura\t{self.unità_misura}\n'
            f'> media\t\t{media:.2f}\n'
            f'> allarme\t{self.stato_allarme}'
        )

    def scostamento_medio(self) -> float:
        if not self.letture:
            return 0.0
        m = self.media_letture()
        return sum(abs(x - m) for x in self.letture) / len(self.letture)


if __name__ == "__main__":
    s = Sensore('sens01', 'Sala A', [28.5, 30.0, 29.5])
    t = SensoreTemperatura('sens02', 'Sala B', [37.0, 38.0], 39.0)
    print(s.descrizione())
    print(t.descrizione())
    t.aggiungi_lettura(38.5)
    print('-> stato_allarme:', t.stato_allarme)
    t.aggiungi_lettura(39.5)
    print('-> stato_allarme:', t.stato_allarme)
    print('Media letture sensore temperatura:', t.media_letture())
    print(t.descrizione())
    print('Scostamento medio:', t.scostamento_medio())
