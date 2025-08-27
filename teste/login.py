import tkinter as tk
from tkinter import messagebox
import banco
from principal import abrir_principal  # função que cria o Toplevel

class LoginFrame(tk.Frame):
    def __init__(self, master, ctrl):
        super().__init__(master)
        self.ctrl = ctrl

        tk.Label(self, text="E-mail:").grid(row=0, column=0, padx=10, pady=10)
        self.email = tk.Entry(self)
        self.email.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
        self.senha = tk.Entry(self, show="*")
        self.senha.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self, text="Entrar", command=self.validar)\
            .grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self, text="Cadastrar novo usuário",
                  command=lambda: ctrl.mostrar("Cadastro"))\
            .grid(row=3, column=0, columnspan=2)

    def validar(self):
        email = self.email.get()
        senha = self.senha.get()
        if not email or not senha:
            messagebox.showwarning("Atenção", "Preencha e-mail e senha!")
            return
        if banco.verificar_login(email, senha):
            messagebox.showinfo("Sucesso", "Login realizado!")
            self.ctrl.withdraw()          # esconde a janela de login/cadastro
            abrir_principal(self.ctrl)    # cria Toplevel e passa referência
        else:
            messagebox.showerror("Erro", "E-mail ou senha inválidos!")
