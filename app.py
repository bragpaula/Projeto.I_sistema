from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-palavra-secreta'

ongs = [
        {"nomeong": "Casa Do Bem", "descricao": "A Casa do Bem desenvolve ações humanitárias sociais através da educação, esporte, lazer, cultura e cidadania."},
        {"nomeong": "Mãos Atadas", "descricao": "A Casa do Bem desenvolve ações humanitárias sociais através da educação, esporte, lazer, cultura e cidadania."},
        {"nomeong": "Instituto Uniau", "descricao": "A Casa do Bem desenvolve ações humanitárias sociais através da educação, esporte, lazer, cultura e cidadania."}
    ]

def salvar_dados(tipo, nome, username, email, password, telefone, bairro):
    with open('dados.txt', 'a') as f:
        f.write(f'{tipo},{nome},{username},{email},{password},{telefone},{bairro}\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ongs')
def lista_ongs():
    return render_template('ongs.html', ongs=ongs)

@app.route('/decisao-cadastro', methods=['GET', 'POST'])
def decisao_cadastro():
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        if tipo == 'voluntario':
            return render_template('cadastro-voluntario.html')
        elif tipo =='ong':
            return render_template('cadastro-ong.html')
            
    return render_template('decisao-cadastro.html')

@app.route('/cadastro-ong', methods=['GET', 'POST'])
def cadastro_ong():
    if request.method == 'POST':
        nomeong = request.form['nomeong']
        descricao = request.form['descricao']
        
        # Adiciona a nova ONG à lista
        ongs.append({"nomeong": nomeong, "descricao": descricao})
        
        # Redireciona para a lista de ONGs
        return redirect(url_for('lista_ongs'))
    
    return render_template('cadastro-ong.html')

@app.route('/cadastro-voluntario', methods=['GET','POST'])
def cadastro_voluntario():
    if request.method == 'POST':
        nome = request.form['nome']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        telefone = request.form['telefone']
        bairro = request.form['bairro']
        salvar_dados( nome, username, email, password, telefone, bairro)

        return redirect(url_for('index'))
    return render_template('cadastro-voluntario.html')


@app.route('/index2', methods=['GET','POST'])
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
        flash('Login ou senha inválidos')
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



    

if __name__ == '__main__':
    app.run(debug=True)