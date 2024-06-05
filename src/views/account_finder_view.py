import os
from typing import Dict

class AccountFinderView:
    def find_account_view(self) -> Dict:

        os.system('clear || cls')

        print('Login na Conta:'.center(70, '-') + '\n')
        account_number = input('Numero da Conta: ')
        password = input('Senha: ')

        account = {
            'account_number': account_number,
            'password': password
        }

        return account
    
    def find_account_success(self, message: Dict) -> None:
        os.system('clear || cls')

        success_message = f'''{message["message"]}
        
        Conta: {message["account"].number_account}
        Saldo: R$ {message["account"].balance:.2f}
        '''

        print(success_message)

    def find_account_error(self, error: str) -> None:
        os.system('clear || cls')
        
        fail_message = f'''Falha ao buscar conta:
        
            Erro: {error}
        '''

        print(fail_message)