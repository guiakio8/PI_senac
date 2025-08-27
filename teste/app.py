import tkinter as tk
from login import LoginFrame
from cadastro import CadastroFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Consultorio")
        # self.geometry("350x380")
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # instancias das telas
        self.frames = {
            "Login": LoginFrame(container, self),
            "Cadastro": CadastroFrame(container, self)
        }
        for f in self.frames.values():
            f.grid(row=0, column=0, sticky="nsew")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.mostrar("Login")

    def mostrar(self, nome):
        self.frames[nome].tkraise()


if __name__ == "__main__":
    App().mainloop()
