from src import views
from src import controllers

def account_register_constructor():
    account_register_view = views.AccountRegisterView()
    account_register_controller = controllers.AccountRegisterController()

    #Pega as informações da nova conta na view
    new_account_information = account_register_view.register_account_view()

    #Envia as informações para o controller, que irá validar e criar a conta
    response = account_register_controller.register(new_account_information)

    #Verifica se a conta foi criada com sucesso
    if response['success']:
        account_register_view.register_account_success(response['message'])

        #Criando senha
        password = account_register_view.password_view()
        response = account_register_controller.password(response['message']['attributes'], password)

        #Verifica se a senha foi criada com sucesso
        if response['success']:
            account_register_view.password_success(response['message'])
        else:
            account_register_view.password_fail(response['error'])

    else:
        account_register_view.register_account_fail(response['error'])    