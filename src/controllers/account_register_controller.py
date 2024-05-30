from typing import Dict
from src import models

class AccountRegisterController:
    def register(self, new_account_informartions: Dict) -> Dict:

        try:
            self.__validate_fields(new_account_informartions)

            new_account_informartions['account_number'] = self.__number_account_generator()

            self.__saving_account(new_account_informartions)
            response = self.__format_response(new_account_informartions)
            
            return {'success': True, 'message': response}
        
        except Exception as error:
            return {'success': False, 'error': str(error)}
         

    def __validate_fields(self, new_account_informartions: Dict) -> None:

        # Verifica se o campo nome é uma string
        if not isinstance(new_account_informartions['name'], str):
            raise Exception('Campo nome inválido!')
        
        # Verifica se o campo idade é um número
        try: int(new_account_informartions['age'])       
        except: raise Exception('Campo idade inválido!')

        # Verifica se a idade é maior que 18
        if int(new_account_informartions['age']) < 18:
            raise Exception('Para criar uma conta é necessário ter mais de 18 anos!')
        
    def __number_account_generator(self) -> int:
        return len(models.data.account_data.account) + 1

    def __saving_account(self, new_account_informartions: Dict) -> None:
        name = new_account_informartions['name']
        age = new_account_informartions['age']
        account_number = new_account_informartions['account_number']
        
        new_person = models.classes.Person(name, age)
        new_account = models.classes.Account(new_person)
        new_account.number_account = account_number

        models.data.account_data.register_account(new_account)

    def __format_response(self, new_account_informartions: Dict) -> Dict:
        return {
            'message': 'Conta criada com sucesso!',
            'count': '1',
            'type': 'account',
            'attributes': new_account_informartions
        }	