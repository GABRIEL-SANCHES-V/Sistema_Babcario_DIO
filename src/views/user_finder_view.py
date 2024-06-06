import os
from typing import Dict

class UserFinderView:
    # Coletando informações do usuário para encontrar no Banco de Dados
    def user_information(self):
        os.system('clear || cls')

        print('Encontrar Usuário'.center(70, '-'))

        cpf = input('Digite o CPF: ')

        return cpf
    
    #Tela de sucesso ao encontrar o usuário
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

    #Tela de falha ao encontrar o usuário
    def user_finder_fail(self, error: str):
        os.system('clear || cls')

        fail_message = f'''Erro ao encontrar usuário:

        Erro: {error}
        '''
        print(fail_message)