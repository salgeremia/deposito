class Cat:
    def __init__(self, name: str) -> None:
        self.__name = name
    
    def __str__(self) -> str:
        return f'Cat name: {self.__name}'
    
    def mew(self) -> None:
        print('Meooow')


c = Cat('Sibilla')
c.mew()
print(c)

