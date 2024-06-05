from typing import Dict
from src import models

class AccountFinderController:
    def find_by_account(self, account_finder_information: Dict) -> Dict:
        try:
            # Validate campos
            self.__validate_fields(account_finder_information)
            # Procura conta
            account = self.__find_account(account_finder_information)
            # Formata resposta
            response = self.__format_response(account)
            return {'success': True, 'message': response}
        
        except Exception as error:
            return {'success': False, 'error': str(error)}
    
    def __validate_fields(self, account_finder_information: Dict) -> None:          
        try: int(account_finder_information['account_number'])
        except: raise Exception('Campo Numero da Conta Invalido!')
        
    def __find_account(self, account_finder_information: Dict) -> models.classes.Account:
        account_number = int(account_finder_information['account_number'])
        password = account_finder_information['password']

        account = models.data.account_data.find_account_by_account_number(password, account_number)

        if account is None:
            raise Exception('Conta não encontrada!')
        
        return account

    def __format_response(self, account: models.classes.Account) -> Dict:
        return {
            'message': 'Login realizado com sucesso!',
            'account': account
        }
        
