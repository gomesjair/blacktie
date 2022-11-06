from flask import Flask, render_template, request


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
    return render_template('cadastro.html', titulo='Cadastro')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    usuario = Usuario(nome, email, senha)

@app.route('/suporte')
def suporte():
    return render_template('suporte.html', titulo='Suporte')

@app.route('/cap')
def cap():
    render_template('cap.html', titulo='CAP')

@app.route('/nap')
def cap():
    render_template('nap.html', titulo='NAP')

@app.route('/conta')
def cap():
    render_template('conta.html', titulo='Minha Conta')

@app.route('/termos')
def termos():
    render_template('termos.html', titulo='Termos')



app.run(debug=True)
