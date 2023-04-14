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
    create_html
    return render_template('agendamento_consulta.html')

@app.route('/cadastro_profissional', methods=['GET', 'POST'])
def cadastro_profissional():
    if request.method == 'POST':
        tipo_profissional = request.form.get('tipo_profissional')
        nome_profissional = request.form.get('nome_profissional')
        sobrenome_profissional = request.form.get('sobrenome_profissional')
        if tipo_profissional and nome_profissional and sobrenome_profissional:
            query = f"""INSERT INTO Profissionais(TipoProfissional, Nome, Sobrenome)
            VALUES
                ('{tipo_profissional}', '{nome_profissional}', '{sobrenome_profissional}')"""
            insert_db(query)
    return redirect(url_for('home'))

@app.route('/cadastro_paciente', methods=['GET', 'POST'])
def cadastro_paciente():
    if request.method == 'POST':
        nome_paciente = request.form.get('nome_paciente')
        sobrenome_paciente = request.form.get('sobrenome_paciente')
        #sexo_paciente = request.form.get('sexo_paciente')
        if nome_paciente and sobrenome_paciente:
            query = f"""INSERT INTO Pacientes(Nome, Sobrenome)
            VALUES
                ('{nome_paciente}', '{sobrenome_paciente}')"""
            insert_db(query)
    return redirect(url_for('home'))

@app.route('/agendamento_consulta', methods=['GET', 'POST'])
def agendamento_consulta():
    if request.method == 'POST':
        nome_paciente = request.form.get('nome_paciente')
        nome_profissional = request.form.get('nome_profissional')
        data_consulta = request.form.get('data_consulta')
        if nome_paciente and nome_profissional and data_consulta:
            query = f"""INSERT INTO Pacientes(Nome, Sobrenome)
            VALUES
                ('{nome_paciente}', '{nome_profissional}')"""
            insert_db(query)
    return redirect(url_for('home'))

def create_html():

    html_profissionais = ''
    nomes_profissionais = select_db('SELECT Nome From Profissionais')
    for i in nomes_profissionais:
        html_profissionais += f'''<option value="{i[0]}">{i[0]}</option>
        '''

    html_pacientes = ''
    nomes_pacientes = select_db('SELECT Nome From Pacientes')
    for i in nomes_pacientes:
        html_pacientes += f'''<option value="{i[0]}">{i[0]}</option>
        '''

    html_final = f"""<head>
        <title>Agendar consulta</title>
        <body>
            <h1>Agendar consulta</h1>
            <hr>
            <form action="/agendar_consulta" method="post">
                <table>
                    <tr>
                        <label for="nome-paciente">Nome do Paciente:</label>
                        <select id="tipo" name="nome_paciente" multiple>
                            {html_pacientes}
                        </select>
                    </tr>
                    <tr>
                        <label for="nome-profissional">Nome do Profissional:</label>
                        <select id="tipo" name="nome_profissional" multiple>
                            {html_profissionais}
                        </select>
                    </tr>
                    <tr>
                        <label for="data">Data Consulta:</label>
                        <input type="datetime-local" id="data" name="data_consulta">
                    </tr>
                    <tr class="button">
                        <button type="submit">Agendar</button>
                    </tr>
                </table>
            </form>
            <form action="/">
                <input type="submit" value="Ir para página inicial" />
            </form>
        </body>
    </head>"""

    with open('templates\\agendamento_consulta.html', 'W') as file:
        file.write(html_final)

if __name__ == '__main__':
    app.run(debug=True)
