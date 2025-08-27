import sqlite3

def conectar():
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            curso TEXT,
            cep TEXT,
            email TEXT UNIQUE,
            senha TEXT
        )
    """)
    conn.commit()
    conn.close()

def inserir(nome, idade, curso, cep, email, senha):
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO alunos (nome, idade, curso, cep, email, senha)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nome, idade, curso, cep, email, senha))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verificar_login(email, senha):
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos WHERE email=? AND senha=?", (email, senha))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def listar():
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    dados = cursor.fetchall()
    conn.close()
    return dados

def excluir(id):
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE id=?", (id,))
    conn.commit()
    reorganizar_ids(conn)  # Reorganiza os IDs após a exclusão
    conn.close()

def reorganizar_ids(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos ORDER BY id")
    alunos = cursor.fetchall()
    novo_id = 1
    for aluno in alunos:
        cursor.execute("UPDATE alunos SET id=? WHERE id=?", (novo_id, aluno[0]))
        novo_id += 1
    conn.commit()

def editar(id, nome, idade, curso, cep, email=None, senha=None):
    conn = sqlite3.connect("alunos.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE alunos SET nome=?, idade=?, curso=?, cep=?, email=?, senha=? WHERE id=?
    """, (nome, idade, curso, cep, email, senha, id))
    conn.commit()
    conn.close()

