import tkinter as tk


class Tela1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Você está na Tela 1", font=("Arial", 16)).pack(pady=20)

        tk.Button(
            self,
            text="Ir para Tela 2",
            command=lambda: controller.mostrar_tela("Tela2")
        ).pack()


class Tela2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Você está na Tela 2", font=("Arial", 16)).pack(pady=20)

        tk.Button(
            self,
            text="Voltar para Tela 1",
            command=lambda: controller.mostrar_tela("Tela1")
        ).pack()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Exemplo com duas telas")
        self.geometry("300x180")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.telas = {}
        for Tela in (Tela1, Tela2):
            nome = Tela.__name__
            frame = Tela(parent=container, controller=self)
            self.telas[nome] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela("Tela1")

    def mostrar_tela(self, nome):
        self.telas[nome].tkraise()


if __name__ == "__main__":
    App().mainloop()
