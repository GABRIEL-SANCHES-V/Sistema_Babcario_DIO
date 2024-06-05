import os
from typing import Dict

class UserFinderView:
    def user_information(self):
        os.system('clear || cls')

        print('Encontrar Usuário'.center(30, '-') + '\n')

        cpf = input('Digite o CPF: ')

        return cpf
    
    def user_finder_success(self, message: Dict):
        os.system('clear || cls')

        success_message = f'''{message['message']}

        Nome: {message['name']}
        Data de Nascimento: {message['birth_date']}
        CPF: {message['cpf']}
        Logradouro: {message['public_place']}
        Bairro: {message['neighborhood']}
        Cidade/Estado: {message['city_state']}
        '''
        print(success_message)

    def user_finder_fail(self, error: str):
        os.system('clear || cls')

        fail_message = f'''Erro ao encontrar usuário:

        Erro: {error}
        '''
        print(fail_message)