import os
from typing import Dict

class DepositView:
    #Tela para saber o valor do deposito na conta corrente
    def deposit_screen(self) -> float:
        os.system('clear || cls')

        print('Tela de Depositar:'.center(70, '-'))

        value = input('\nValor: R$ ')
        
        return value
    
    #Tela para exibir a mensagem de sucesso ao depositar na conta corrente
    def deposit_success(self, account: Dict) -> None:
        os.system('clear || cls')

        success_message = f'''{account['message']}
        \nSaldo Atual: {account['attributes'].balance}'''

        print(success_message)

    #Tela para exibir a mensagem de erro ao depositar na conta corrente
    def deposit_error(self, error: str) -> None:
        os.system('clear || cls')

        fail_message = f'''Erro ao depositar!
        
        Erro: {error}'''

        print(fail_message)