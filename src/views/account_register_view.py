import os
from typing import Dict

class AccountRegisterView:

    def register_account_view(self) -> Dict:
        os.system("clear || cls")

        print("Criar Nova Conta:")
        name = input("Nome: ")
        age = input("Idade: ")

        new_account = {
            'name': name,
            'age': age,
            'account_number': 0,
            'balance': 0.0,
            'number_withdraws': None,
            'extract': None,
        }

        return new_account
    
    def register_account_success(self, message: Dict) -> None:
        os.system("clear || cls")
        
        success_message = f'''{message['message']}

        Tipo: {message['type']}
        Registros: {message['count']}
        Infos:
            Nome: {message['attributes']['name']}
            Idade: {message['attributes']['age']}
            Numero da Conta: {message['attributes']['account_number']}
            Saldo: {message['attributes']['balance']}
            Saques: {message['attributes']['number_withdraws']}
            Número de Saques Diarios: 3
        '''
        print(success_message)

    def register_account_fail(self, error: str) -> None:
        os.system("clear || cls")
        
        fail_message = f'''Erro ao criar conta:
        
            Erro: {error}
        '''
        print(fail_message)