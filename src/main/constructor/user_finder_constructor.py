from src import views
from src import controllers

def user_finder_constructor():
    user_finder_view = views.UserFinderView()
    user_finder_controller = controllers.UserFinderController()

    #Pega as informações do usuário na view
    user_information = user_finder_view.user_information()

    #Busca o usuário no sistema pelo controller, aplicando as regras de negocio e retornando a resposta
    response = user_finder_controller.user_finder(user_information)

    #Verifica se a busca foi bem sucedida ou não e para poder exibir a mensagem adequada na view
    if response['success']:
        user_finder_view.user_finder_success(response['message'])
    else:
        user_finder_view.user_finder_fail(response['error'])
