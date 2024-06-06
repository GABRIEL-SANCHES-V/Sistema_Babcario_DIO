from .person import Person
from typing import Dict

#Classe para a criação da conta corrente, com os atributos de pessoa, agência, número da conta, saldo, senha, número de saques e extrato
class Account:
    def __init__(self, person: Person) -> None:
        self.person = person
        self.agency = '0001'
        self.number_account = 0
        self.balance = 0.0
        self.password = ''
        self.number_withdraws = 0
        self.extract = []

    #Método para depositar na conta corrente
    def deposit(self, deposit) -> None:
        self.balance += float(deposit)
        self.__add_extract({'type': 'Depósito', 'value': deposit})

    #Método para sacar da conta corrente
    def withdraw(self, withdraw) -> None:
        self.balance -= float(withdraw)
        self.number_withdraws += 1
        self.__add_extract({'type': 'Saque', 'value': withdraw})

    #Método para adicionar transações no extrato
    def __add_extract(self, transaction: Dict) -> None:
        self.extract.append(transaction)