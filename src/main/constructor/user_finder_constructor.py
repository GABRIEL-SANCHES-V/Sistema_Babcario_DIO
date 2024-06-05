from src import views
from src import controllers

def user_finder_constructor():
    user_finder_view = views.UserFinderView()
    user_finder_controller = controllers.UserFinderController()

    user_information = user_finder_view.user_information()
    response = user_finder_controller.user_finder(user_information)

    if response['success']:
        user_finder_view.user_finder_success(response['message'])
    else:
        user_finder_view.user_finder_fail(response['error'])
