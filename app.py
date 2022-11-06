from flask import Flask, render_template, request, re


#classe para o formulario de cadasto
class Usuario:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

#app flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo='Home')
    
@app.route('/login')
def login():
    return render_template('cadastro.html', titulo_login='Cadastro')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    usuario = Usuario(nome, email, senha)


app.run(debug=True)
