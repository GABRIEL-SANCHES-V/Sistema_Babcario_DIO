
class OptionsMenu():

    def home_menu():
        message = '''Menu de Opções:
        1 - Criar Conta
        2 - Entrar na Conta
        5 - Sair'''

        print(message)

        commands = input(f'Digite o número da opção desejada: ')

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