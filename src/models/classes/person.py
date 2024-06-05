from .address import Address
class Person:
    def __init__(self, name: str, birth_date: str, cpf: str, address: Address) -> None:
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf
        self.address = address

    

    