import os
from typing import Dict

class AccountFinderView:
    def find_account_view(self) -> Dict:

        os.system('clear || cls')

        print('Login na Conta:')
        name = input('Nome: ')
        account_number = input('Numero da Conta: ')

        account = {
            'name': name,
            'age': None,
            'account_number': account_number,
            'balance': None,
            'number_withdraws': None,
            'extract': None,
        }

        return account
    
    def find_account_success(self, message: Dict) -> None:
        os.system('clear || cls')

        success_message = 'Login realizado com sucesso!'

        print(success_message)

    def find_account_error(self, error: str) -> None:
        os.system('clear || cls')
        
        fail_message = f'''Falha ao buscar conta:
        
            Erro: {error}
        '''

        print(fail_message)