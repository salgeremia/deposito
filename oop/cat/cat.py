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

# let's try changing the cat's name in another way
c.__name = 'Trilly'
print(c)
# as you can see, it doesn't work!

# even though a (dangerous) way exists:
c._Cat__name = 'Trilly'
print(c)
# now that you know, forget it.