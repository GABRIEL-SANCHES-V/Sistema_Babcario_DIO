from src import views
from src import controllers
from src import models

def deposit_constructor(account: models.classes.Account) -> None:
    deposit_view = views.DepositView()
    deposit_controllers = controllers.DepositController()

    value = deposit_view.deposit_screen()
    response = deposit_controllers.deposit(account, value)

    if response['success']:
        deposit_view.deposit_success(response['message'])

    else:
        deposit_view.deposit_error(response['error'])
    