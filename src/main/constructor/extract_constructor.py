from src import models
from src import controllers
from src import views

def extract_constructor(account: models.classes.Account):
    extract_view = views.ExtractView()
    extract_controller = controllers.ExtractController()

    response = extract_controller.extract(account)

    if response['Success']:
        extract_view.extract_success(response['message'])
    else:
        extract_view.extract_fail(response['error'])
