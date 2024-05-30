import os
from typing import Dict

class WithdrawView():
    def withdraw_screen(self):
        os.system('clear || cls')

        print('Tela de saque'.center(30))
        value = input('\nDigite o valor do saque: R$ ')

        return value
    
    def withdraw_sucess(self, response: Dict) -> None:
        os.system('clear || cls')

        sucess_message = f'''{response['message']}

        Valor do Saque: {response['value']}

        Novo Saldo: R$ {response['attributes'].balance:.2f}'''

        print(sucess_message)

    def withdraw_error(self, response: str) -> None:
        os.system('clear || cls')

        error_message = f'''Erro ao realizar saque!
        
        Erro: {response}'''

        print(error_message)