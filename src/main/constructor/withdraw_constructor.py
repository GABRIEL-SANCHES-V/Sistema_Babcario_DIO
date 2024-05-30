from src import views
from src import models
from src import controllers

def withdraw_constructor(account: models.classes.Account):
    withdraw_view = views.WithdrawView()
    withdraw_controller = controllers.WithdrawController()

    value = withdraw_view.withdraw_screen()
    response = withdraw_controller.withdraw(account, value)

    if response['success']:
        withdraw_view.withdraw_sucess(response['message'])
    else:
        withdraw_view.withdraw_error(response['error'])