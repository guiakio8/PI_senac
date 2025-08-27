import tkinter as tk
from tkinter import messagebox
from banco import *

conectar()

def abrir_principal(janela_login):
    """Cria a janela principal; recebe a referência do Tk oculto."""
    janela = tk.Toplevel()
    janela.title("Sistema consultorio")
    # janela.geometry("400x450")
    container = tk.Frame()
    container.pack(fill="both", expand=True)


    # widgets -------------
    tk.Label(janela, text="Nome:").pack()
    ent_nome = tk.Entry(janela); ent_nome.pack()

    tk.Label(janela, text="Idade:").pack()
    ent_idade = tk.Entry(janela); ent_idade.pack()

    tk.Label(janela, text="Curso:").pack()
    ent_curso = tk.Entry(janela); ent_curso.pack()

    lista = tk.Listbox(janela, width=45); lista.pack(pady=11)

    # funções internas -------------
    def listar_alunos():
        lista.delete(0, tk.END)
        for a in listar():
            lista.insert(tk.END, f"{a[0]} - {a[1]} ({a[2]} anos) - {a[3]}")

    def salvar():
        n, i, c = ent_nome.get(), ent_idade.get(), ent_curso.get()
        if n and i and c:
            try:
                inserir(n, int(i), c, None, None, None)
                listar_alunos(); limpar()
            except Exception as e:
                messagebox.showerror("Erro", e)
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")

    def excluir_aluno():
        sel = lista.curselection()
        if sel:
            item = lista.get(sel)
            id_ = int(item.split(" ")[0])
            if messagebox.askyesno("Confirmar", "Excluir aluno?"):
                excluir(id_); listar_alunos(); limpar()

    def editar_aluno():
        sel = lista.curselection()
        if sel:
            item = lista.get(sel)
            id_ = int(item.split(" ")[0])
            n, i, c = ent_nome.get(), ent_idade.get(), ent_curso.get()
            if n and i and c:
                try:
                    editar(id_, n, int(i), c, None, None, None)
                    listar_alunos(); limpar()
                except Exception as e:
                    messagebox.showerror("Erro", e)

    def limpar():
        ent_nome.delete(0, tk.END)
        ent_idade.delete(0, tk.END)
        ent_curso.delete(0, tk.END)

    # botões -------------
    tk.Button(janela, text="Salvar", command=salvar).pack(pady=4)
    tk.Button(janela, text="Editar", command=editar_aluno).pack(pady=4)
    tk.Button(janela, text="Excluir", command=excluir_aluno).pack(pady=4)

    listar_alunos()

    # quando fechar, mostra de novo o login/cadastro
    def ao_fechar():
        janela_login.deiconify()
        janela.destroy()
    janela.protocol("WM_DELETE_WINDOW", ao_fechar)
