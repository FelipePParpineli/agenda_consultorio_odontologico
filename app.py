from flask import Flask, render_template, request, url_for, redirect
from db import conectar_db, insert_db, select_db

app = Flask(__name__)

cursor = conectar_db

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/cadastrar_profissional')
def cadastrar_profissional():
    return render_template('cadastro_profissional.html')

@app.route('/cadastrar_paciente')
def cadastrar_paciente():
    return render_template('cadastro_paciente.html')

@app.route('/agendar_consulta', methods=['GET', 'POST'])
def agendar_consulta():
    return render_template('agendamento_consulta.html')

@app.route('/cadastro_profissional', methods=['GET', 'POST'])
def cadastro_profissional():
    if request.method == 'POST':
        tipo_profissional = request.form.get('tipo_profissional')
        nome_profissional = request.form.get('nome_profissional')
        sobrenome_profissional = request.form.get('sobrenome_profissional')
        data_nascimento = request.form.get('data_nascimento')
        endereco = request.form.get('endereco_profissional')
        if tipo_profissional and nome_profissional and sobrenome_profissional:
            query = f"""INSERT INTO Profissionais(TipoProfissional, Nome, Sobrenome, DataNascimento, Endereco)
            VALUES
                ('{tipo_profissional}', '{nome_profissional}', '{sobrenome_profissional}', '{data_nascimento}', '{endereco}')"""
            insert_db(query)
    return redirect(url_for('home'))

@app.route('/cadastro_paciente', methods=['GET', 'POST'])
def cadastro_paciente():
    if request.method == 'POST':
        nome_paciente = request.form.get('nome_paciente')
        sobrenome_paciente = request.form.get('sobrenome_paciente')
        sexo_paciente = request.form.get('sexo_paciente')
        endereco_paciente = request.form.get('endereco_paciente')
        if nome_paciente and sobrenome_paciente:
            query = f"""INSERT INTO Pacientes(Nome, Sobrenome, Sexo, Endereco)
            VALUES
                ('{nome_paciente}', '{sobrenome_paciente}', '{sexo_paciente}', '{endereco_paciente}')"""
            insert_db(query)
    return redirect(url_for('home'))

@app.route('/agendamento_consulta', methods=['GET', 'POST'])
def agendamento_consulta():
    if request.method == 'POST':
        nome_paciente = request.form.get('nome_paciente')
        nome_profissional = request.form.get('nome_profissional')
        data_consulta = request.form.get('data_consulta')
        if nome_paciente and nome_profissional and data_consulta:
            query = f"""INSERT INTO Consultas(nome_Profissional, nome_Paciente, Horario)
            VALUES
                ('{nome_profissional}', '{nome_paciente}', '{data_consulta}')"""
            insert_db(query)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
