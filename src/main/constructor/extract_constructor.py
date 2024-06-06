from src import models
from src import controllers
from src import views

def extract_constructor(account: models.classes.Account):
    extract_view = views.ExtractView()
    extract_controller = controllers.ExtractController()

    #Envia as informações para o controller, que irá validar e buscar o extrato da conta corrente
    response = extract_controller.extract(account)

    #Verifica se o extrato foi encontrado com sucesso, se sim, exibe as informações do extrato na view
    if response['Success']:
        extract_view.extract_success(response['message'])
    else:
        extract_view.extract_fail(response['error'])
