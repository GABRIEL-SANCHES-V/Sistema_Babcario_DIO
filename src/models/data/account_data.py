from src import models
from .person_data import person_1, person_2, person_3

class __AccountData:
    def __init__(self) -> None:
        self.accounts = []

    def register_account(self, account: models.classes.Account) -> None:
        self.accounts.append(account)

    def find_account_by_account_number(self, password: str, account_number: int) -> models.classes.Account:
        for account in self.accounts:
            if int(account.number_account) == account_number:
                if account.password == password:
                    return account
                else:
                    raise Exception('Senha Incorreta!')
        return None
    
    def update_account(self, account: models.classes.Account) -> None:
        for account_data in self.accounts:
            if account_data.number_account == account.number_account:
                account_data = account
                break
    
account_1 = models.classes.Account(person_1)
account_1.number_account = 1
account_1.password = '1111'

account_2 = models.classes.Account(person_2)
account_2.number_account = 2
account_2.password = '2222'

account_3 = models.classes.Account(person_3)
account_3.number_account = 3
account_3.password = '3333'

account_data = __AccountData()

account_data.register_account(account_1)
account_data.register_account(account_2)
account_data.register_account(account_3)
