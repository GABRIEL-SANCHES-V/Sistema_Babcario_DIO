from typing import Dict
from src import models

class UserFinderController:
    def user_finder(self, cpf: str) -> Dict:
        try:
            self.__validate_cpf(cpf)
            user = self.__search_user(cpf)
            response = self.__format_response(user)
            return {'success': True, 'message': response}
        except Exception as error:
            return {'success': False, 'error': str(error)}

    def __validate_cpf(self, cpf: str):
        if not len(cpf) == 11:
            raise Exception('CPF inválido, número de digite inferior a 11')
        
        if not cpf.isdigit():
            raise Exception('CPF inválido, contém letras')
        
    def __search_user(self, cpf: str) -> models.classes.Person:
        user = models.data.person_data.find_person_by_cpf(cpf)

        if user is None:
            raise Exception('Usuário não encontrado')
        
        return user
        
    def __format_response(self, user: models.classes.Person) -> Dict:
        return {
            'message': 'Usuário encontrado com sucesso!',
            'type': 'user',
            'name': user.name,
            'birth_date': user.birth_date,
            'cpf': user.cpf,
            'public_place': user.address.public_place,
            'neighborhood': user.address.neighborhood,
            'city_state': user.address.city_state,
            'atributes': user
        }