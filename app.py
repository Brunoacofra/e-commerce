from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://testuser:toledo22@localhost:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column('usu_codigo', db.Integer, primary_key=True)
    email = db.Column('usu_email', db.String(100))
    user = db.Column('usu_username', db.String(100))
    senha = db.Column('usu_senha', db.String(100))

    def __init__(self, user, email, senha):
        self.email = email
        self.user = user
        self.senha = senha

class categoria(db.Model):
	id = db.Column('cat_codigo', db.Integer, primary_key=True)
	nome = db.Column('cat_nome'),db.String(200)

	def __init__(self,nome):
		self.nome = nome
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/cadastro/usuario')
def usuario():
    return render_template('cadastroUsuario.html', usuarios = Usuario.query.all(), titulo="Cadastro de usuarios")

@app.route('/cadastro/anuncio')
def ads():
    return render_template('ads.html')

@app.route('/ads/pergunta')
def pergunta():
    return render_template('perguntas.html')

@app.route('/ads/compra')
def compra():
    print('Anuncio de compra')
    return ''

@app.route('/ads/favoritos')
def favoritos():
    print('Inserido aos favoritos')
    return ''

@app.route('/config/categoria')
def categoria():
    return render_template('cadastroCategoria.html')

@app.route('/relatorio/venda')
def relatorioCompra():
    return render_template('relatorioCompra.html')

@app.route('/relatorio/compra')
def relatorioVenda():
    return render_template('relatorioVenda.html')

@app.route("/cadastro/cadastroUsuario", methods=['POST'])
def cad():
    usuario = Usuario(
        request.form.get('user'),
        request.form.get('email'),
        request.form.get('senha')
    )
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('usuario'))
@app.route("cadastro/cadastroCategoria",methods=['POST'])
	def cadcat():
		categoria = categoria(request.form.get('cat'))
		deb.session.add(categoria)
		db.session.commit()
		return redirect(url_for('categoria'))
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)