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
    


account_data = __AccountData()
