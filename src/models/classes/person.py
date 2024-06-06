from .address import Address
class Person:
    # Classe que representa uma pessoa, com as características de nome, data de nascimento, cpf e endereço(que também é um classe).
    def __init__(self, name: str, birth_date: str, cpf: str, address: Address) -> None:
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf
        self.address = address

    

    