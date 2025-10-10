class Car:
    def __init__(self, make: str, model: str, year: int, max_speed: int, speed = 0) -> None:
        self.make = make                # marca dell'auto
        self.model = model              # modello
        self.year = year                # anno di produzione
        self.max_speed = max_speed      # velocità massima
        self.__set_speed(speed)         # velocità corrente

    def __str__(self) -> str:
        return f'{self.make} {self.model} viaggia alla velocità di {self.__speed} km/h.'

    def __set_speed(self, speed: int) -> None:
        '''Imposta la velocità dell'auto, che può andare da zero a max_speed.'''
        if speed < 0: 
            self.__speed = 0
        elif speed > self.max_speed:
            self.__speed = self.max_speed
        else:
            self.__speed = speed

    def change_speed(self, diff: int) -> None:
        '''Modifica la velocità corrente dell'auto.'''
        self.__set_speed(self.__speed + diff)  

    def get_speed(self) -> int:
        '''Restituisce la velocità corrente dell'auto.'''
        return self.__speed

'''
c = Car('fiat', 'uno', 1975, 140, 70)   # creazione oggetto 
print(c)
c.change_speed(80)                      # cambio di velocità per superare la velocità massima
print(c)
c.change_speed(-30)                     # cambio di velocità
print(c)
vel_attuale = c.get_speed()             # memorizzo la velocità attuale
print(f'La velocità attuale dell\'automobile è di {vel_attuale} km/h.')
'''
d = Car('fiat', 'uno', 1975, 140, 20)   # creazione oggetto 
print(d)
d.change_speed(170)
print(d)
d.change_speed(-40)
print(d)
d.model = 'panda'
print(d)