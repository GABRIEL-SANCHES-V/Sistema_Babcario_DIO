from src.models import classes

# Classe para manipular os dados das pessoas
class __PersonData:
    def __init__(self) -> None:
        self.person = []

    # Registra uma nova pessoa no banco de dados
    def register_person(self, person: classes.Person) -> None:
        self.person.append(person)

    # Encontra uma pessoa no banco de dados pelo CPF
    def find_person_by_cpf(self, cpf: str) -> classes.Person:
        for person in self.person:
            if person.cpf == cpf:
                return person
        return None
    
    # Valida se o CPF já está cadastrado no banco de dados
    def validate_cpf(self, cpf: str) -> bool:
        for person in self.person:
            if person.cpf == cpf:
                return False
        return True
    

# Banco dr Dados de Pessoas Improvisado - Este é um exemplo de dados que poderiam ser carregados de um banco de dados seguindo o modelo sigleton

address_1 = classes.Address('Rua 1', 'Bairro 1', 'Cidade 1 - Estado 1')
person_1 = classes.Person('João', '01/01/2000', '12345678901', address_1)

address_2 = classes.Address('Rua 2', 'Bairro 2', 'Cidade 2 - Estado 2')
person_2 = classes.Person('Maria', '02/02/2000', '12345678902', address_2)

address_3 = classes.Address('Rua 3', 'Bairro 3', 'Cidade 3 - Estado 3')
person_3 = classes.Person('José', '03/03/2000', '12345678903', address_3)

person_data = __PersonData()

person_data.register_person(person_1)
person_data.register_person(person_2)
person_data.register_person(person_3)
