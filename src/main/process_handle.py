from src.main import constructor

#Arquivo que gerencia o sistema como um todo
def start() -> None:
    #Inicia o sistema
    while True:
        #Menu principal
        command = constructor.home_menu()

        #Opção 1 - Cadastro de Usuário
        if command == '1': constructor.user_register_constructor()

        #Opção 2 - Busca de Usuário
        elif command == '2': constructor.user_finder_constructor()

        #Opção 3 - Cadastro de Conta
        elif command == '3': constructor.account_register_constructor()

        #Opção 4 - Login
        elif command == '4': 
            account = constructor.account_find_constructor()
            
            #Se a conta foi encontrada
            if account is not None:
                while True:

                    #Menu da conta
                    command = constructor.account_menu()

                    #Opção 1 - Saldo
                    if command == '1': constructor.balance_constructor(account)

                    #Opção 2 - Depósito
                    elif command == '2': constructor.deposit_constructor(account)

                    #Opção 3 - Saque
                    elif command == '3': constructor.withdraw_constructor(account)  

                    #Opção 4 - Extrato
                    elif command == '4': constructor.extract_constructor(account) 

                    #Opção 5 - Sair
                    elif command == '5':
                        print('\nSair\n')
                        break

                    #Opção inválida
                    else: print('\nOpção invalida\n')

        #Opção 5 - Sair
        elif command == '5':
            print('\nSair\n')
            exit()

        #Opção inválida
        else:
            print('\nOpção invalida\n')