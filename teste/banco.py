import sqlite3
conn = None

def conectar():
    global conn
    conn = sqlite3.connect("alunos.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS alunos
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT, idade INTEGER, curso TEXT,
                  cep TEXT, email TEXT UNIQUE, senha TEXT)""")
    conn.commit()

def inserir(nome, idade, curso, cep, email, senha):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO alunos (nome,idade,curso,cep,email,senha) VALUES (?,?,?,?,?,?)",
                  (nome, idade, curso, cep, email, senha))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def verificar_login(email, senha):
    c = conn.cursor()
    c.execute("SELECT * FROM alunos WHERE email=? AND senha=?", (email, senha))
    return c.fetchone()

def listar():
    return conn.cursor().execute("SELECT * FROM alunos").fetchall()

def excluir(id_):
    conn.cursor().execute("DELETE FROM alunos WHERE id=?", (id_,))
    conn.commit()

def editar(id_, nome, idade, curso, cep, email, senha):
    conn.cursor().execute("""UPDATE alunos SET nome=?, idade=?, curso=?,
                             cep=?, email=?, senha=? WHERE id=?""",
                          (nome, idade, curso, cep, email, senha, id_))
    conn.commit()
