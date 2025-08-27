import tkinter as tk
from tkinter import messagebox
import banco  
import main

def validar_login():
    email = entry_email.get()
    senha = entry_senha.get()

    # Validação de campos obrigatórios
    if not email or not senha:
        messagebox.showwarning("Atenção", "Preencha e-mail e senha!")
        return

    # Verifica login no banco de dados
    usuario = banco.verificar_login(email, senha)
    if usuario:
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        root.destroy()  # Fecha a tela de login
        main.abrir_interface()  # Abre a interface principal
    else:
        messagebox.showerror("Erro", "E-mail ou senha inválidos!")

def abrir_cadastro():
    root.destroy()  # Fecha a tela de login
    import cadastro  # Abre a tela de cadastro


# Criação da interface de login
root = tk.Tk()
root.title("Tela de Login")

tk.Label(root, text="E-mail:").grid(row=0, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
entry_senha = tk.Entry(root, show="*")
entry_senha.grid(row=1, column=1, padx=10, pady=10)

btn_login = tk.Button(root, text="Entrar", command=validar_login)
btn_login.grid(row=2, column=0, columnspan=2, pady=10)

btn_cadastrar = tk.Button(root, text="Cadastrar Novo Usuário", command=abrir_cadastro)
btn_cadastrar.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()