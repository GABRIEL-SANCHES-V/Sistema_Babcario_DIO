from typing import Dict
from src import models
from datetime import datetime

class UserRegisterController:
    def user_register(self, new_user_information: Dict) -> Dict:
        try:
            self.__validate_fields(new_user_information)
            self.__saving_user(new_user_information)
            response = self.__format_response(new_user_information)
            return {'success': True, 'message': response}
        
        except Exception as error:
            return {'success': False, 'error': str(error)}
        
    #Valida os campos do novo usuário.
    def __validate_fields(self, new_user_information: Dict) -> None:
        if not isinstance(new_user_information['name'], str):
            raise Exception('Campo Nome Inválido!')
        
        if not isinstance(new_user_information['birth_date'], str):
            raise Exception('Campo Data de Nascimento Inválido!')
        
        self.__validate_birth_date(new_user_information['birth_date'])
        
        self.__validate_cpf(new_user_information['cpf'])
    
    #Valida a data de nascimento, de acordo com o número de caracteres e se está no formato correto.
    def __validate_birth_date(self, birth_date: str) -> None:
        if len(birth_date) != 10:
            raise Exception('Data de Nascimento Inválida! (dd/mm/aaaa)')
        
        if not birth_date[2] == '/' and birth_date[5] == '/':
            raise Exception('Data de Nascimento Inválida! (dd/mm/aaaa)')

    #Valida o CPF, de acordo com o número de de caracteres e se já existe no sistema.
    def __validate_cpf(self, cpf: str) -> None:
        if len(cpf) != 11:
            raise Exception('CPF Inválido!')
        
        if not models.data.person_data.validate_cpf(cpf):
            raise Exception('CPF já cadastrado!')


    #Salva o novo usuário no sistema, enviando para models para ser guardado no banco de dados(que até o momento é uma gambiara). 
    def __saving_user(self, new_user_information: Dict) -> None:
        name = new_user_information['name']
        birth_date = new_user_information['birth_date']
        cpf = new_user_information['cpf']
        public_place = new_user_information['address']['public_place']
        neighborhood = new_user_information['address']['neighborhood']
        city_state = new_user_information['address']['city_state']

        address = models.classes.Address(public_place, neighborhood, city_state)
        new_user = models.classes.Person(name, birth_date, cpf, address)
        
        models.data.person_data.register_person(new_user)

    #Formata a resposta para ser exibida na view.
    def __format_response(self, new_user_information: Dict) -> Dict:
        new_user = {
            'message': 'Usuário criado com sucesso!',
            'attributes': new_user_information
        }

        return new_user