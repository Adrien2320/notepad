from view import MyView
from model import Data
from controller import Controller


class App:
    def __init__(self, title: str):
        self.view = MyView(title=title)
        self.model = Data()
        self.controller = Controller(self.view, self.model)
        self.view.set_controller(self.controller)

        self.view.start_my_view()


if __name__ == "__main__":
    app = App("Note")
