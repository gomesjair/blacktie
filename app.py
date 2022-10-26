from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def home():
    return render_template('index.html', titulo='Home')
    
@app.route('/login')
def login():
    return render_template('cadastro.html', titulo_login='Cadastro')

app.run()
