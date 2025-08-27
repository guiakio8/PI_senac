import tkinter as tk
from tkinter import messagebox
from banco import conectar, inserir, listar, excluir, editar

conectar()

def abrir_principal(janela_login):
    """Cria a janela principal; recebe a referência do Tk oculto."""
    win = tk.Toplevel()
    win.title("Cadastro de Alunos")
    win.geometry("400x450")

    # widgets -------------
    tk.Label(win, text="Nome:").pack()
    ent_nome = tk.Entry(win); ent_nome.pack()

    tk.Label(win, text="Idade:").pack()
    ent_idade = tk.Entry(win); ent_idade.pack()

    tk.Label(win, text="Curso:").pack()
    ent_curso = tk.Entry(win); ent_curso.pack()

    lista = tk.Listbox(win, width=50); lista.pack(pady=10)

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
    tk.Button(win, text="Salvar", command=salvar).pack(pady=4)
    tk.Button(win, text="Editar", command=editar_aluno).pack(pady=4)
    tk.Button(win, text="Excluir", command=excluir_aluno).pack(pady=4)

    listar_alunos()

    # quando fechar, mostra de novo o login/cadastro
    def ao_fechar():
        janela_login.deiconify()
        win.destroy()
    win.protocol("WM_DELETE_WINDOW", ao_fechar)
