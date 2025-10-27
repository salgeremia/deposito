class Character:
    ''' _____________________________________________________
        - name  : str
        - age   : int
        _____________________________________________________
        - __init__(name: str, age: int) -> None
        + get_name() -> str
        + get_age() -> int
        _____________________________________________________
    '''
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def __str__(self) -> str:
        return f'{self.get_name()} ha {self.get_age()} anni'

    def get_name(self) -> str:
        return self.__name
    
    def get_age(self) -> int:
        return self.__age
    
class Jedi(Character):
    ''' _____________________________________________________
        - rank  : str
        _____________________________________________________
        - __init__(name: str, age: int, rank: str) -> None
        + get_rank() -> str
        _____________________________________________________
    '''
    def __init__(self, name: str, age: int, rank: str) -> None:
        super().__init__(name, age)
        self.__rank = rank

    def __str__(self) -> str:
        str_character = super().__str__()
        return f'{str_character} ed è {self.get_rank()}'

    def get_rank(self) -> str:
        return self.__rank


c = Character('Han Solo', 35)
print(c)
j = Jedi('Yoda', 900, 'Gran Maestro')
print(j)

# Verifico se j è un Character
print(f'{j.get_name()} è un Character: {isinstance(j, Character)}')