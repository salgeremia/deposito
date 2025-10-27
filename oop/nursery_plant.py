class NurseryPlant:
    ''' _____________________________________________________
        + plant_id  :   int
        + name      :   str
        - pot_size  :   int
        + is_sold   :   bool
        _____________________________________________________
        - __init__(plant_id: int, name: str) -> None
        + set_pot_size(pot_size: int) -> None
        + get_pot_size() -> int
        + transplant(pot_size: int) -> None
        + sell() -> None
        + get_plant_info() -> str 
        _____________________________________________________
    '''
    def __init__(self, plant_id: int, name: str) -> None:
        self.plant_id = plant_id
        self.name = name
        self.is_sold = False
        self.set_pot_size(-1)
    
    def set_pot_size(self, pot_size: int) -> None:
        if pot_size < 1:
            self.__pot_size = -1
        else: 
            self.__pot_size = pot_size

    def get_pot_size(self) -> int:
        return self.__pot_size
    
    def transplant(self, pot_size: int) -> None:
        self.set_pot_size(pot_size)

    def sell(self) -> None:
        if self.is_sold == False:
            self.is_sold = True
            self.set_pot_size(0)
    
    def get_plant_info(self) -> str:
        if self.is_sold == False:
            return f'Pianta {self.plant_id}: {self.name}, vaso: {self.get_pot_size()}, da vendere'
        else:
            return f'Pianta {self.plant_id}: {self.name}, venduta'


p = NurseryPlant(401, 'rosa')
p.set_pot_size(10)
print(p.get_plant_info())
p = NurseryPlant(432, 'cactus')
p.sell()
print(p.get_plant_info())