from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def home():
    return render_template('index.html', titulo='home')
    
@app.route('/login')
def login():
    return render_template('login.html', titulo='login')

app.run()
