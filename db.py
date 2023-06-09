import pyodbc

def conectar_db():
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=DESKTOP-82SB2ES;"
        "Database=ProjetoAgenda;"
    )

    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()
    return cursor

def select_db(query):
    cursor = conectar_db()
    query_insert = query
    result = cursor.execute(query_insert)
    row = cursor.fetchone()
    result_select = []
    while row:
        result_select.append(row)
        row = cursor.fetchone()
    return result_select

def insert_db(query):
    cursor = conectar_db()
    query_insert = query
    cursor.execute(query_insert)
    cursor.commit()
