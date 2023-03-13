import ttkbootstrap as ttk
import ttkbootstrap.constants as cttk
from ttkbootstrap.scrolled import ScrolledText


class MyView(ttk.Window):
    def __init__(self):
        super().__init__(themename="superhero")

        self.menu = Menu(self)
        self.block_note = BlockNote(self)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.menu.grid(column=0, row=0, sticky=cttk.EW)
        self.block_note.grid(column=0, row=1, sticky=cttk.NSEW)

    def file_title(self):
        pass

    def apropos(self):
        pass

    def exit(self):
        pass

    def new(self):
        pass

    def open(self):
        pass

    def save(self):
        pass

    def save_as(self):
        pass

    def error_message(self, message: str) -> None:
        pass

    def start_my_view(self) -> None:
        self.mainloop()

    def set_controller(self, value):
        self.controller = value

    def success_message(self, message: str):
        pass


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # icon for button
        self.picture_new = ttk.PhotoImage(file="picture/new.png")
        self.picture_save = ttk.PhotoImage(file="picture/save.png")
        self.picture_save_as = ttk.PhotoImage(file="picture/save_as.png")
        self.picture_open = ttk.PhotoImage(file="picture/open.png")
        self.picture_information = ttk.PhotoImage(file="picture/information.png")
        self.picture_exit = ttk.PhotoImage(file="picture/exit.png")
        # widget
        self.bt_new = ttk.Button(self, image=self.picture_new)
        self.bt_save = ttk.Button(self, image=self.picture_save)
        self.bt_save_as = ttk.Button(self, image=self.picture_save_as)
        self.bt_open = ttk.Button(self, image=self.picture_open)
        self.bt_information = ttk.Button(self, image=self.picture_information)
        self.bt_exit = ttk.Button(self, image=self.picture_exit)
        # position
        self.bt_new.pack(side=cttk.LEFT)
        self.bt_save.pack(side=cttk.LEFT)
        self.bt_save_as.pack(side=cttk.LEFT)
        self.bt_open.pack(side=cttk.LEFT)
        self.bt_exit.pack(side=cttk.RIGHT)
        self.bt_information.pack(side=cttk.RIGHT)


class BlockNote(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.text = ScrolledText(self, hbar=True)
        self.text.pack(fill=cttk.BOTH, expand=True)


if __name__ == "__main__":
    MyView().start_my_view()
