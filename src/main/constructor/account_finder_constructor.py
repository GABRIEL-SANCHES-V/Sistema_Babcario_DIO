from src import views
from src import controllers

def account_find_constructor():
    account_finder_view = views.AccountFinderView()
    account_finder_controller = controllers.AccountFinderController()

    #Pega as informações da conta a ser buscada na view
    account_finder_information = account_finder_view.find_account_view()

    #Envia as informações para o controller, que irá validar e buscar a conta
    response = account_finder_controller.find_by_account(account_finder_information)

    #Exibe a resposta na view
    if response['success']:
        account_finder_view.find_account_success(response['message'])
        return response['message']['account']
        

    else:
        account_finder_view.find_account_error(response['error'])
