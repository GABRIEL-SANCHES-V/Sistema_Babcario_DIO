from src import views

def balance_constructor(account):
    balance_view = views.BalanceView()
    #Exibe o saldo da conta corrente com a conta encontrada após o login
    balance_view.display_balance(account.balance)