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

    c.execute("""CREATE TABLE IF NOT EXISTS medicos
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT,
                  idade INTEGER,
                  funcao TEXT,
                  nome_usuario TEXT UNIQUE,  -- UNIQUE para evitar duplicatas de usuário
                  senha TEXT)""")

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

def inserir_medico(nome, idade, funcao, nome_usuario, senha):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO medicos (nome,idade,funcao,nome_usuario,senha) VALUES (?,?,?,?,?)",
                  (nome, idade, funcao, nome_usuario, senha))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def verificar_login(email, senha):
    c = conn.cursor()
    c.execute("SELECT * FROM medicos WHERE nome_usuario=? AND senha=?", (email, senha))
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
