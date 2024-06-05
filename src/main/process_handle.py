from src.main import constructor

def start() -> None:

    while True:
        command = constructor.home_menu()

        if command == '1':
            constructor.user_register_constructor()

        elif command == '2':
            constructor.user_finder_constructor()

        elif command == '3':
            constructor.account_register_constructor()

        elif command == '4':
            account = constructor.account_find_constructor()

            if account is not None:
                while True:
                    command = constructor.account_menu()

                    if command == '1':
                        constructor.balance_constructor(account)

                    elif command == '2':
                        constructor.deposit_constructor(account)

                    elif command == '3':
                        constructor.withdraw_constructor(account)
                    
                    elif command == '4':
                        constructor.extract_constructor(account)
                    
                    elif command == '5':
                        print('\nSair\n')
                        break

                    else:
                        print('\nOpção invalida\n')

        elif command == '5':
            print('\nSair\n')
            exit()

        else:
            print('\nOpção invalida\n')