import tkinter as tk
from tkinter import messagebox
import banco  

def cadastrar_usuario():
    nome = entry_nome.get()
    idade = entry_idade.get()
    curso = entry_curso.get()
    cep = entry_cep.get()
    email = entry_email.get()
    senha = entry_senha.get()

    if not nome or not idade or not curso or not cep or not email or not senha:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    try:
        idade = int(idade)
    except ValueError:
        messagebox.showerror("Erro", "Idade deve ser um número válido!")
        return

    if len(cep) != 8 or not cep.isdigit():
        messagebox.showerror("Erro", "CEP deve conter 8 dígitos numéricos!")
        return

    if "@" not in email or "." not in email:
        messagebox.showerror("Erro", "E-mail inválido!")
        return

    if len(senha) < 6:
        messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres!")
        return

    if banco.inserir(nome, idade, curso, cep, email, senha):
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        root.destroy()
        import login  
    else:
        messagebox.showerror("Erro", "E-mail já cadastrado!")

def voltar_login():
    root.destroy()
    import login  


root = tk.Tk()
root.title("Tela de Cadastro")

tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Idade:").grid(row=1, column=0, padx=10, pady=10)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Curso:").grid(row=2, column=0, padx=10, pady=10)
entry_curso = tk.Entry(root)
entry_curso.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="CEP:").grid(row=3, column=0, padx=10, pady=10)
entry_cep = tk.Entry(root)
entry_cep.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="E-mail:").grid(row=4, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=4, column=1, padx=10, pady=10)

tk.Label(root, text="Senha:").grid(row=5, column=0, padx=10, pady=10)
entry_senha = tk.Entry(root, show="*")
entry_senha.grid(row=5, column=1, padx=10, pady=10)

btn_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_usuario)
btn_cadastrar.grid(row=6, column=0, columnspan=2, pady=10)

btn_voltar = tk.Button(root, text="Voltar", command=voltar_login)
btn_voltar.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()