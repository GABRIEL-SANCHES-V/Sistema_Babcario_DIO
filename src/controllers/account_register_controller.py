from typing import Dict
from src import models
from datetime import datetime

class AccountRegisterController:
    def register(self, new_account_informartions: str) -> Dict:
        try:
            self.__validate_cpf(new_account_informartions)
            user = self.__find_user(new_account_informartions)
            current_account = self.__create_account(user)
            self.__saving_account(current_account)
            response = self.__format_response(current_account)
            
            return {'success': True, 'message': response}
        
        except Exception as error:
            return {'success': False, 'error': str(error)}

    #Associa a senha a conta e salvando no Banco de Dados
    def password(self, account: models.classes.Account, password: str) -> Dict:
        try:
            account.password = password
            models.data.account_data.update_account(account)
            return {'success': True, 'message': 'Senha criada com sucesso!'}
        except Exception as error:
            return {'success': False, 'error': str(error)}
    
    #Valida o CPF, verificando se o CPF tem 11 digitos e se é um número
    def __validate_cpf(self, new_account_informartions: str) -> None:
        if not len(new_account_informartions) == 11:
            raise Exception('CPF inválido, número de digite inferior a 11')
        
        if not new_account_informartions.isdigit():
            raise Exception('CPF inválido, contém letras')

    #Procura o usuário pelo CPF no Banco de Dados
    def __find_user(self, cpf: str) -> models.classes.Person:
        user = models.data.person_data.find_person_by_cpf(cpf)

        if user is None:
            raise Exception('Usuário não encontrado!')
        
        return user
             
    #Gera o número da conta corrente, com base na quantidade de contas já criadas
    def __number_account_generator(self) -> int:
        return len(models.data.account_data.accounts) + 1
    
    #Cria a conta corrente
    def __create_account(self, user: models.classes.Person) -> models.classes.Account:
        current_account = models.classes.Account(user)
        current_account.number_account = self.__number_account_generator()
        return current_account

    #Salva a conta no Banco de Dados, no caso, em um banco de dados improvisado que está no models
    def __saving_account(self, new_account_informartions: models.classes.Account) -> None:
        models.data.account_data.register_account(new_account_informartions)
    
    #Formata a resposta para ser exibida na view
    def __format_response(self, new_account_informartions: models.classes.Account) -> Dict:
        return {
            'message': 'Conta criada com sucesso!',
            'type': 'Conta Corrente',
            'name': new_account_informartions.person.name,
            'birth_date': new_account_informartions.person.birth_date,
            'cpf': new_account_informartions.person.cpf,
            'public_place': new_account_informartions.person.address.public_place,
            'neighborhood': new_account_informartions.person.address.neighborhood,
            'city_state': new_account_informartions.person.address.city_state,
            'agency': new_account_informartions.agency,
            'number_account': new_account_informartions.number_account,
            'balance': new_account_informartions.balance,
            'attributes': new_account_informartions
        }	