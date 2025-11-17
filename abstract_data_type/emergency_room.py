# Esercizio pag. 353 n. 4 - emergency_room

class Coda:
    def __init__(self) -> None:
        self.__coda = list()

    def __str__(self) -> str:
        return str(self.__coda)
    
    def aggiungi(self, elemento) -> None:
        self.__coda.append(elemento)

    def rimuovi(self):
        return self.__coda.pop(0)


class Persona:
    def __init__(self, nome: str, cognome: str) -> None:
        self.__nome = nome
        self.__cognome = cognome
    
    def get_cognome(self) -> str:
        return self.__cognome
    

class Paziente(Persona):
    def __init__(self, nome: str, cognome: str, codice: int) -> None:
        super().__init__(nome, cognome)
        self.__codice = codice
    ''' Il parametro codice assume i valori:
        0 -> codice ROSSO
        1 -> codice GIALLO
        2 -> codice VERDE
        3 -> codice BIANCO
    '''
    
    def get_codice(self):
        return self.__codice


class EmergencyRoom:
    def __init__(self) -> None:
        self.__room = [Coda(), Coda(), Coda(), Coda()]

    def get_info(self) -> str:
        info = ''
        for i in range(len(self.__room)):
            info += f'{i} -> {self.__room[i]}\n'
        return info
    
    def arrivo_paziente(self, paziente: Paziente) -> None:
        self.__room[paziente.get_codice()].aggiungi(paziente.get_cognome())

    def visita_paziente(self):
        precedenza = 0
        while precedenza < 4:
            if self.__room[precedenza]:
                return self.__room[precedenza].rimuovi()
            precedenza += 1


paziente_1 = Paziente('Harry', 'Potter', 1)
paziente_2 = Paziente('Lord', 'Voldemort', 0)
paziente_3 = Paziente('Albus', 'Silente', 3)
paziente_4 = Paziente('Ron', 'Weasley', 2)
paziente_5 = Paziente('Hermione', 'Granger', 3)
paziente_6 = Paziente('Severus', 'Piton', 0)

emergency_room = EmergencyRoom()
emergency_room.arrivo_paziente(paziente_1)
emergency_room.arrivo_paziente(paziente_2)
emergency_room.arrivo_paziente(paziente_3)
emergency_room.arrivo_paziente(paziente_4)
emergency_room.arrivo_paziente(paziente_5)
emergency_room.arrivo_paziente(paziente_6)

print(f'\nSITUAZIONE INIZIALE:\n{emergency_room.get_info()}')

print('INIZIANO LE VISITE...')
print(f'- {emergency_room.visita_paziente()}')
print(f'- {emergency_room.visita_paziente()}')

print(f'\nSITUAZIONE ATTUALE:\n{emergency_room.get_info()}')

print('CONTINUANO LE VISITE...')
print(f'- {emergency_room.visita_paziente()}')
print(f'- {emergency_room.visita_paziente()}')
print(f'- {emergency_room.visita_paziente()}')

# PS: l'implementazione proposta NON prevede la generazione casuale del codice del paziente.