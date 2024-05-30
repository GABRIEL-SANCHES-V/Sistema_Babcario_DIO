from src.models import classes


class __AccountData:
    def __init__(self) -> None:
        self.account = []

    def register_account(self, account: classes.Account) -> None:
        self.account.append(account)

    def find_account_by_account(self, name: str, account_number: int) -> classes.Account:
        for account in self.account:
            if account.person.name == name and account.number_account == account_number:
                return account
        return None
    
    def update_account(self, account: classes.Account) -> None:
        for account_data in self.account:
            if account_data.number_account == account.number_account:
                account_data = account
                break
    

# Dados de Contas
    
account_1 = classes.Account(classes.Person('João', 20))
account_1.number_account = 1
account_1.balance = 1000.0

account_2 = classes.Account(classes.Person('Maria', 30))
account_2.number_account = 2

account_3 = classes.Account(classes.Person('José', 40))
account_3.number_account = 3

account_data = __AccountData()

account_data.register_account(account_1)
account_data.register_account(account_2)
account_data.register_account(account_3)