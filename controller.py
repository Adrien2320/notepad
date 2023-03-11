from view import MyView
from model import Data


class Controller:
    def __init__(self, view: MyView, model: Data):
        self.view = view
        self.model = model

    def save(self, text) -> None:
        try:
            self.model.text = text
            self.model.save()
            self.view.success_message("Text bien enregistré !")
        except ValueError:
            self.view.error_message("Text non enregistré !")
