from src.models import classes

class __PersonData:
    def __init__(self) -> None:
        self.person = []

    def register_person(self, person: classes.Person) -> None:
        self.person.append(person)

    def find_person_by_cpf(self, cpf: str) -> classes.Person:
        for person in self.person:
            if person.cpf == cpf:
                return person
        return None
    

# Dados de Pessoas - Este é um exemplo de dados que poderiam ser carregados de um banco de dados seguindo o modelo sigletom

Person_1 = classes.Person('João', '01/01/2000', '12345678901', {'public_place': 'Rua 1', 'neighborhood': 'Bairro 1', 'city_state': 'Cidade 1/UF'})
Person_2 = classes.Person('Maria', '02/02/2000', '12345678902', {'public_place': 'Rua 2', 'neighborhood': 'Bairro 2', 'city_state': 'Cidade 2/MG'})
Person_3 = classes.Person('José', '03/03/2000', '12345678903', {'public_place': 'Rua 3', 'neighborhood': 'Bairro 3', 'city_state': 'Cidade 3/RG'})

person_data = __PersonData()

person_data.register_person(Person_1)
person_data.register_person(Person_2)
person_data.register_person(Person_3)