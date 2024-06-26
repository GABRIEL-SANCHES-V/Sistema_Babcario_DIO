from typing import Dict
from src import models

class DepositController:
    def deposit(self, account: models.classes.Account, deposit) -> Dict:
        try:
            self.__validate_fields(deposit)
            account = self.__deposit(account, deposit)
            response = self.__format_responsive(account)
            return {'success': True, 'message': response}
        
        except Exception as error:
            return {'success': False, 'error': str(error)}
        
    #Valida os campos de entrada
    def __validate_fields(self, deposit) -> None:
       try: float(deposit)
       except: raise Exception('Campo valor inválido!')

       if float(deposit) <= 0:
           raise Exception('O valor do depósito deve ser maior que zero!')
    
    #Realiza o depósito na conta corrente e atualiza no Banco de Dados 
    def __deposit(self, account: models.classes.Account, deposit):
        account.deposit(deposit)
        models.data.account_data.update_account(account)
        return account
    
    #Formata a resposta para ser exibida na view
    def __format_responsive(self, account: models.classes.Account) -> Dict:
        return {
            'message': 'Depósito realizado com sucesso!',
            'operation': 'Depósito',
            'attributes': account
        }