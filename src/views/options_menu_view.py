
class OptionsMenu():

    def home_menu():
        print('Menu Principal:'.center(30, '-'))
        
        message = '''
        1 - Cadastrar Usuário
        2 - Encontrar Usuário
        3 - Cadastrar Conta Corrente
        4 - Entrar na Conta
        5 - Sair'''

        print(message)

        commands = input(f'\nDigite o número da opção desejada: ')

        return commands
    
    def account_menu():
        message = '''\nMenu de Conta:
        1 - Ver Saldo
        2 - Depositar
        3 - Sacar
        4 - Extrato
        5 - Sair'''

        print(message)

        commands = input(f'Digite o número da opção desejada: ')

        return commands