import os
from typing import Dict

class UserRegisterView:
    # Coletando informações do usuário para cadastro
    def user_information(self) -> Dict:
        os.system('clear || cls')

        print('Cadastrar Usuário'.center(70, '-'))

        name = input('Nome: ')
        birth_date = input('Data de Nascimento (DD/MM/AAAA): ')
        cpf = input('CPF: ')

        print('')
        
        print('Enereço'.center(30, '-'))
        public_place = input('Logradouro: ')
        neighborhood = input('Bairro: ')
        city_state = input('Cidade/Sigla do Estado: ')

        address = {
            'public_place': public_place,
            'neighborhood': neighborhood,
            'city_state': city_state,
        }

        new_user = {
            'name': name,
            'birth_date': birth_date,
            'cpf': cpf,
            'address': address
        }

        return new_user
    
    #Tela de sucesso no cadastro do usuário
    def register_user_success(self, response: Dict) -> None:
        os.system('clear || cls')

        success_message = f'''{response['message']}

        Nome: {response['attributes']['name']}
        Data de Nascimento: {response['attributes']['birth_date']}
        CPF: {response['attributes']['cpf']}
        Logradouro: {response['attributes']['address']['public_place']}
        Bairro: {response['attributes']['address']['neighborhood']}
        Cidade/Estado: {response['attributes']['address']['city_state']}
        '''

        print(success_message)

    #Tela de falha no cadastro do usuário
    def register_user_fail(self, error: str) -> None:
        os.system('clear || cls')

        fail_message = f'''Erro ao cadastrar usuário:
        
        Erro: {error}
        '''

        print(fail_message)