from src import views
from src import controllers

def account_register_constructor():
    account_register_view = views.AccountRegisterView()
    account_register_controller = controllers.AccountRegisterController()

    #Pega as informações da nova conta na view
    new_account_information = account_register_view.register_account_view()

    #Envia as informações para o controller, que irá validar e criar a conta
    response = account_register_controller.register(new_account_information)

    #Exibe a resposta na view
    if response['success']:
        account_register_view.register_account_success(response['message'])
    else:
        account_register_view.register_account_fail(response['error'])    