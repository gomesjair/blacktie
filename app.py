from flask import Flask, render_template, request

class Usuario:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

app = Flask(__name__)

@app.route('/inicio')
def home():
    return render_template('index.html', titulo='Home')
    
@app.route('/login')
def login():
    return render_template('cadastro.html', titulo_login='Cadastro')

@app.route('/criar')
def criar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    usuario = Usuario(nome, email, senha)


app.run()
