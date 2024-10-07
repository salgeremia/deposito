class BankAccount:
    def __init__(self, balance: float, holder: str) -> None:
        self.set_balance(balance)
        self.holder = holder

    def __str__(self) -> str:
        return f'{self.holder} = {self.get_balance()}'
    
    def set_balance(self, balance: float) -> None:
        self.__balance = balance

    def get_balance(self) -> float:
        return self.__balance
    
    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        self.__balance -= amount

    
ba = BankAccount(0, 'Geremia')
ba.deposit(1048.50)
ba.withdraw(420)
money = ba.get_balance()
print(money)
