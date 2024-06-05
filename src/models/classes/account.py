from .person import Person
from typing import Dict

class Account:
    def __init__(self, person: Person) -> None:
        self.person = person
        self.agency = '0001'
        self.number_account = 0
        self.balance = 0.0
        self.number_withdraws = 0
        self.extract = []

    def deposit(self, deposit) -> None:
        self.balance += float(deposit)
        self.__add_extract({'type': 'Depósito', 'value': deposit})

    def withdraw(self, withdraw) -> None:
        self.balance -= float(withdraw)
        self.number_withdraws += 1
        self.__add_extract({'type': 'Saque', 'value': withdraw})


    def __add_extract(self, transaction: Dict) -> None:
        self.extract.append(transaction)