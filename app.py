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
   #arrumar aqui dps
    usuario = null

@app.route('/suporte')
def suporte():
    return render_template('suporte.html', titulo='Suporte')

@app.route('/cap')
def cap():
    return render_template('cap.html', titulo='CAP')

@app.route('/nap')
def nap():
    return render_template('nap.html', titulo='NAP')

@app.route('/conta')
def conta():
    return render_template('conta.html', titulo='Minha Conta')

@app.route('/termos')
def termos():
    return render_template('termos.html', titulo='Termos')



app.run(debug=True)
