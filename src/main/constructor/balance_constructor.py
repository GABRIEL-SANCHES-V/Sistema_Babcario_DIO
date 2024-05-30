from src import views
from src import models

def balance_constructor(account):
    balance_view = views.BalanceView()
    balance_view.display_balance(account.balance)