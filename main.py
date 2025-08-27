from login import *
import cadastro as cadastro
import tkinter as tk
from tkinter import messagebox
from banco import conectar, inserir, listar, excluir, editar

# Conecta ao banco de dados ao iniciar o sistema
conectar()

def salvar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    curso = entry_curso.get()

    if nome and idade and curso:
        try:
            inserir(nome, int(idade), curso, cep=None, email=None, senha=None)  # Ajustado para inserir sem email e senha
            listar_pacientes()
            limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao inserir dados: {e}")
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")

def listar_pacientes():
    lista.delete(0, tk.END)
    for aluno in listar():
        lista.insert(tk.END, f"{aluno[0]} - {aluno[1]} ({aluno[2]} anos) - {aluno[3]}")

def excluir_aluno():
    selecionado = lista.curselection()
    if selecionado:
        item = lista.get(selecionado)
        id = int(item.split(" ")[0])
        if messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir o aluno?"):
            excluir(id)
            listar_pacientes()
            limpar_campos()
    else:
        messagebox.showinfo("Atenção", "Selecione um aluno para excluir.")

def editar_aluno():
    selecionado = lista.curselection()
    if selecionado:
        item = lista.get(selecionado)
        id = int(item.split(" ")[0])
        nome = entry_nome.get()
        idade = entry_idade.get()
        curso = entry_curso.get()

        if nome and idade and curso:
            try:
                editar(id, nome, int(idade), curso, cep=None, email=None, senha=None)
                listar_pacientes()
                limpar_campos()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao editar dados: {e}")
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos para editar.")
    else:
        messagebox.showinfo("Atenção", "Selecione um aluno para editar.")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_curso.delete(0, tk.END)

def abrir_interface():
    global entry_nome, entry_idade, entry_curso, lista

    janela = tk.Tk()
    janela.title("Cadastro de Pacientes")
    janela.geometry("400x450")

    tk.Label(janela, text="Nome:").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Idade:").pack()
    entry_idade = tk.Entry(janela)
    entry_idade.pack()

    tk.Label(janela, text="Curso:").pack()
    entry_curso = tk.Entry(janela)
    entry_curso.pack()

    tk.Button(janela, text="Salvar", command=salvar).pack(pady=5)
    tk.Button(janela, text="Editar", command=editar_aluno).pack(pady=5)
    tk.Button(janela, text="Excluir", command=excluir_aluno).pack(pady=5)

    lista = tk.Listbox(janela, width=50)
    lista.pack(pady=10)

    listar_pacientes()

    janela.mainloop()

if __name__ == "__main__":
    abrir_interface()
