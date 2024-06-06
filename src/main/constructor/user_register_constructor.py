from src import views
from src import controllers

def user_register_constructor():
    user_register_view = views.UserRegisterView()
    user_register_constructor = controllers.UserRegisterController()

    #Pega as informações do novo usuário na view
    new_user_information = user_register_view.user_information()
    #Cadastra o novo usuário no sistema pelo controller, aplicando as regras de negocio e retornando a resposta
    response = user_register_constructor.user_register(new_user_information)

    #Verifica se o cadastro foi bem sucedido ou não e para exibir a mensagem adequada
    if response['success']:
        user_register_view.register_user_success(response['message'])
    else:
        user_register_view.register_user_fail(response['error'])