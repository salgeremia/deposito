class Cat:
    def __init__(self, name: str) -> None:
        self.__name = name
    
    def __str__(self) -> str:
        return f'> cat name: {self.__name}'
    
    def meow(self) -> None:
        print('meooow')

    def change_name(self, new_name: str) -> None:
        self.__name = new_name


c = Cat('Sibilla')
print(c)
c.meow()                # Sibilla meows...
c.change_name('Pepe')   # change cat's name from "Sibilla" to "Pepe"
print(c)