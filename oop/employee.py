class Employee:
    def __init__(self, name, surname, salary) -> None:
        self.__name = name
        self.__surname = surname
        self.salary = salary

    def __str__(self) -> str:
        return f'\nDATI DEL DIPENDENTE:\nNome: {self.__name}\nCognome: {self.__surname}\n€{self.salary}'
        
    def payrase(self, amount):
        self.salary += amount

    def set_surname(self, new_surname):
        self.__surname = new_surname


f = Employee('Fausto', 'Velardo', 40_000)
s = Employee('Salvatore', 'Geremia', 15_000)
a = Employee('Andrea', 'Cinocca', 60_000)

print(f, s, a)
s.payrase(40000)
s.set_surname('Rossi')
print(s)