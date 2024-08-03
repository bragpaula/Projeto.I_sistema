from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/sobrenos')
def sobrenos():
    return render_template('sobrenos.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/doacoes')
def doacoes():
    return render_template('doacoes.html')

@app.route('/campanhas')
def campanhas():
    return render_template('campanhas.html')

@app.route('/doar')
def doar():
    return render_template('doar.html')

@app.route('/voluntario')
def voluntario():
    return render_template('voluntario.html')

@app.route('/cadastrarongs')
def cadastrarongs():
    return render_template('cadastrarongs.html')


if __name__ == '__main__':
    app.run()