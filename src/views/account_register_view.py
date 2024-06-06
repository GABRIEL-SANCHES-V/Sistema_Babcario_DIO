import os
from typing import Dict

class AccountRegisterView:
    #Tela para coletano o CPF para vincular a conta corrente com um conta de usuário
    def register_account_view(self):
        os.system("clear || cls")

        print("Criar Conta Corrente:".center(70, '-') + '\n')
        cpf = input("Dígite o CPF para cadastrar a conta corrente: ")

        return cpf
    
    #Tela para exibir a mensagem de sucesso ao criar a conta corrente
    def register_account_success(self, message: Dict) -> None:
        os.system("clear || cls")
        
        success_message = f'''{message['message']}

        Tipo: {message['type']}
        Infos Pessoais:
            Nome: {message['name']}
            Data de Nascimento: {message['birth_date']}
            CPF: {message['cpf']}
            Endereço: {message['public_place']}, {message['neighborhood']}, {message['city_state']}

        Informações da Conta:
            Agência: {message['agency']}
            Número da Conta: {message['number_account']}
            Saldo Inicial: R$ {message['balance']:.2f}
            '''
        
        print(success_message)

        input("Pressione Enter para continuar...")

    #Tela para exibir a mensagem de erro ao criar a conta corrente
    def register_account_fail(self, error: str) -> None:
        os.system("clear || cls")
        
        fail_message = f'''Erro ao criar conta:
        
            Erro: {error}
        '''
        print(fail_message)

    #Tela para a criação da senha para a conta corrente
    def password_view(self):
        os.system("clear || cls")
        
        print("Criar Senha:".center(70, '-') + '\n')
        password = input("Dígite a senha para a conta corrente: ")

        return password
    
    #Tela para exibir a mensagem de sucesso ao criar a senha
    def password_success(self, message: str) -> None:
        os.system("clear || cls")
        
        success_message = f'''{message}
        '''
        
        print(success_message)

    #Tela para exibir a mensagem de erro ao criar a senha
    def password_fail(self, error: str) -> None:
        os.system("clear || cls")
        
        fail_message = f'''Erro ao criar senha:
        
            Erro: {error}
        '''
        print(fail_message)