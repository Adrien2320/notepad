import tkinter as tk
import tkinter.ttk as ttk
import tkinter.constants as ctk
from tkinter import messagebox


class MyView(tk.Tk):
    def __init__(self, title: str):
        super().__init__()
        self.title(title)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(1, weight=1)

        ################################################ menu
        # style
        style_frame = ttk.Style(self)
        style_frame.configure("test.TLabel", background="gray")
        style_save = ttk.Style(self)
        style_save.configure("save.TButton", background="gray", foreground="green")
        style_exit = ttk.Style(self)
        style_exit.configure("exit.TButton", background="gray", foreground="red")
        # widget
        self.save = ttk.Button(
            self, text="Sauvegarder", style="save.TButton", command=self.do_save
        )
        self.exit = ttk.Button(
            self, text="Quitter", command=self.destroy, style="exit.TButton"
        )
        # position
        self.save.grid(columnspan=2, row=0, sticky=ctk.NSEW)
        self.exit.grid(column=2, columnspan=2, row=0, sticky=ctk.NSEW)
        ################################################ text
        self.text = tk.Text(self)
        self.text.grid(columnspan=4, row=1, sticky=ctk.NSEW)
        self.scrollbar_ver = ttk.Scrollbar(self, orient=ctk.VERTICAL)
        self.scrollbar_ver.grid(column=4, row=1, sticky=ctk.E)
        self.scrollbar_hor = ttk.Scrollbar(self, orient=ctk.HORIZONTAL)
        self.scrollbar_hor.grid(columnspan=5, row=2, sticky=ctk.S)
        ################################################ bottom bar
        self.position_text = ttk.Label(self, text="position")
        self.position_text.grid(column=0, row=3, sticky=ctk.W)
        self.zoom_text = ttk.Label(self, text="zoom")
        self.zoom_text.grid(column=1, row=3, sticky=ctk.E)
        self.encoding = ttk.Label(self, text="encoding")
        self.encoding.grid(column=2, row=3, sticky=ctk.E)
        self.format_text = ttk.Label(self, text="format")
        self.format_text.grid(column=3, row=3, sticky=ctk.E)

    def do_save(self):
        try:
            self.controller.save(self.text)
        except AttributeError:
            self.error_message("Erreur Controller !")

    def error_message(self, message: str) -> None:
        messagebox.showerror("Erreur Notepad", message)

    def start_my_view(self) -> None:
        self.mainloop()

    def set_controller(self, value):
        self.controller = value

    def success_message(self, message: str):
        messagebox.showinfo("confirmation notepad", message)
