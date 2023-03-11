import tkinter as tk
import tkinter.ttk as ttk
import tkinter.constants as ctk


class MyView(tk.Tk):

    def __init__(self, title: str):
        super().__init__()
        self.title(title)
        self.columnconfigure()

        self.menu = ttk.Frame(self,style="my.TFrame")
        self.menu.grid(column=0,row=0,sticky=ctk.NSEW)
        # style
        style_frame = ttk.Style(self)
        style_frame.configure("my.TFrame",background="gray")
        style_save = ttk.Style(self)
        style_save.configure("save.TButton",background ="gray", foreground="green")
        style_exit = ttk.Style(self)
        style_exit.configure("exit.TButton",background ="gray", foreground="red")
        # widget
        self.save = ttk.Button(self.menu, text="Sauvegarder", command=MyView.do_save,style="save.TButton")
        self.exit = ttk.Button(self.menu, text="Quitter", command=MyView.do_exit, style="exit.TButton")
        # position
        self.save.pack(side=ctk.LEFT,padx=2)
        self.exit.pack(side=ctk.LEFT)

    class Text(tk.Text):
        def __init__(self,parent):
            super().__init__(parent)
            self.pack()

    class BottomBar(ttk.Frame):
        def __init__(self,parent):
            super().__init__(parent)
            self.pack(side=ctk.BOTTOM)

    def do_save(self):
        pass

    def do_exit(self):
        pass

    def show_message(self, message: str, color: str) -> None:
        pass

    def start_my_view(self) -> None:
        self.mainloop()

    def set_controller(self, value):
        self.controller = value
