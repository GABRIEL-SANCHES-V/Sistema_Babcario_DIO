from src import views
from src import controllers
from src import models

def deposit_constructor(account: models.classes.Account) -> None:
    deposit_view = views.DepositView()
    deposit_controllers = controllers.DepositController()

    #Pega o valor do depósito na view
    value = deposit_view.deposit_screen()

    #Envia o valor do depósito para o controller, que irá validar e realizar o depósito
    response = deposit_controllers.deposit(account, value)

    #Verifica se o depósito foi realizado com sucesso, se sim, exibe as informações da conta na view
    if response['success']:
        deposit_view.deposit_success(response['message'])

    else:
        deposit_view.deposit_error(response['error'])
    