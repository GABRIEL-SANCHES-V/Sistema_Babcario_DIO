from typing import Dict
from src import models

LIMIT_WITHDRAWS = 3
MAX_WITHDRAW = 500

class WithdrawController:

    def withdraw(self, account: models.classes.Account, withdraw) -> dict:
        try:
            self.__validate_fields(withdraw, account)
            account = self.__withdraw(account, withdraw)
            response = self.__format_responsive(account, withdraw)
            return {'success': True, 'message': response}
        
        except Exception as error:
            return {'success': False, 'error': str(error)}
        
    def __validate_fields(self, withdraw, account: models.classes.Account) -> None:
        try: float(withdraw)
        except: raise Exception('Campo valor inválido!')
            
        if account.number_withdraws >= LIMIT_WITHDRAWS:
            raise Exception('Limite de saques atingido!')
        
        if float(withdraw) <= 0:
            raise Exception('O valor do saque deve ser maior que zero!')
        
        if float(withdraw) > account.balance:
            raise Exception('Saldo insuficiente!')
        
        if float(withdraw) > MAX_WITHDRAW:
            raise Exception('Valor máximo de saque é R$ 500,00!')
        
    def __withdraw(self, account: models.classes.Account, withdraw):
        account.withdraw(withdraw)
        models.data.account_data.update_account(account)
        return account
    
    def __format_responsive(self, account: models.classes.Account, withdraw) -> Dict:
        return {
            'message': 'Saque realizado com sucesso!',
            'operation': 'Saque',
            'value': f'R$ {float(withdraw):.2f}',
            'attributes': account
        }

