from src import views
from src import models
from src import controllers

def withdraw_constructor(account: models.classes.Account):
    withdraw_view = views.WithdrawView()
    withdraw_controller = controllers.WithdrawController()

    #Pega o valor do saque na view
    value = withdraw_view.withdraw_screen()

    #Envia o valor do saque para o controller, que irá validar e realizar o saque
    response = withdraw_controller.withdraw(account, value)

    #Verifica se o saque foi realizado com sucesso, se sim, exibe as informações da conta na view
    if response['success']:
        withdraw_view.withdraw_sucess(response['message'])
    else:
        withdraw_view.withdraw_error(response['error'])