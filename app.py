from view import MyView

class App():

    def __init__(self,title : str):
        self.view = MyView(title=title)


        self.view.start_my_view()


if __name__ == '__main__':
    app = App("Note")