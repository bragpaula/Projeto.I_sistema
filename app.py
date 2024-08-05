from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-palavra-secreta'

def salvar_dados(tipo, nome, username, email, password, telefone, bairro):
    with open('dados.txt', 'a') as f:
        f.write(f'{tipo},{nome},{username},{email},{password},{telefone},{bairro}\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/acessoverific', methods=['POST'])
def acessoverific():
    usuario = request.form['usuario']
    senha = request.form['senha']
    if usuario == 'Jepale' and senha == 'apso1234':
        return redirect(url_for('index2'))
    else: 
        flash('login ou senha inválidos')
        flash('Tente novamente')
    return redirect(url_for('login'))

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

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        tipo = request.form['tipo']
        nome = request.form['nome']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        telefone = request.form['telefone']
        bairro = request.form['bairro']
        salvar_dados(tipo, nome, username, email, password, telefone, bairro)
        return redirect(url_for('login'))
    return render_template('cadastro.html')
    

if __name__ == '__main__':
    app.run()