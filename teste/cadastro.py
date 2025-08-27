import tkinter as tk
from tkinter import messagebox
import banco


class CadastroFrame(tk.Frame):
    def __init__(self, master, ctrl):
        super().__init__(master)
        self.ctrl = ctrl

        labels = ["Nome", "Idade", "Função", "Usuario", "Senha"]
        self.ent = {}
        for i, rot in enumerate(labels):
            tk.Label(self, text=f"{rot}:").grid(row=i, column=0, padx=10, pady=5, sticky="e")
            show = "*" if rot == "Senha" else ""
            e = tk.Entry(self, show=show)
            e.grid(row=i, column=1, padx=10, pady=5)
            self.ent[rot.lower()] = e

        tk.Button(self, text="Cadastrar", command=self.cadastrar) \
            .grid(row=6, column=0, columnspan=2, pady=8)
        tk.Button(self, text="Voltar", command=lambda: ctrl.mostrar("Login")) \
            .grid(row=7, column=0, columnspan=2)

    def cadastrar(self):
        nome = self.ent["nome"].get()
        idade = self.ent["idade"].get()
        funcao = self.ent["função"].get()
        usuario = self.ent["usuario"].get()
        senha = self.ent["senha"].get()

        if not all([nome, idade, funcao, usuario, senha]):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        if not idade.isdigit():
            messagebox.showerror("Erro", "Idade deve ser numérica!")
            return
        if len(usuario) < 5:
            messagebox.showerror("Erro", "Nome de usuario deve conter no mínimo 5 caracteres!")
            return
        if len(senha) < 6:
            messagebox.showerror("Erro", "Senha com mínimo 6 caracteres!")
            return
        if banco.inserir_medico(nome, int(idade), funcao, usuario, senha):
            messagebox.showinfo("Sucesso", "Usuário cadastrado!")
            self.ctrl.mostrar("Login")
        else:
            messagebox.showerror("Erro", "Usuário já cadastrado!")
