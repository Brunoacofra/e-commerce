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

class Categoria(db.Model):
    id = db.Column('cat_codigo', db.Integer, primary_key=True)
    nome = db.Column('cat_nome', db.String(200))

    def __init__(self, nome):
        self.nome = nome

class Anuncio(db.Model):
    __tablename__ = "anuncio"
    id = db.Column('ads_id', db.Integer, primary_key=True)
    nome = db.Column('ads_titulo', db.String(256))
    desc = db.Column('ads_descricao', db.String(256))
    qtd = db.Column('ads_qtd', db.Integer)
    preco = db.Column('ads_preco', db.Float)
    cat_id = db.Column('ads_cat_id', db.Integer, db.ForeignKey("categoria.cat_codigo"))
    usu_id = db.Column('ads_usu_id', db.Integer, db.ForeignKey("usuario.usu_codigo"))

    def __init__(self, nome, desc, qtd, preco, cat_id, usu_id):
        self.nome = nome
        self.desc = desc
        self.qtd = qtd
        self.preco = preco
        self.cat_id = cat_id
        self.usu_id = usu_id

@app.errorhandler(404)
def paginanaoencontrada(error):
    return render_template('png404.html')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/usuarios")
def listar_usuarios():
    return render_template('usuarios.html', usuarios=Usuario.query.all(), titulo="Usuários")

@app.route("/usuario/detalhar/<int:id>")
def buscar_usuario(id):
    usuario = Usuario.query.get(id)
    return usuario.user

@app.route("/usuario/editar/<int:id>", methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = Usuario.query.get(id)
    if request.method == 'POST':
        usuario.user = request.form.get('user')
        usuario.email = request.form.get('email')
        usuario.senha = request.form.get('senha')
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('listar_usuarios'))

    return render_template('editar_usuario.html', usuario=usuario, titulo="Editar Usuário")

@app.route("/usuario/deletar/<int:id>")
def deletar_usuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('listar_usuarios'))

@app.route('/cadastro/usuario', methods=['POST'])
def cadastrar_usuario():
    usuario = Usuario(
        request.form.get('user'),
        request.form.get('email'),
        request.form.get('senha')
    )
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('listar_usuarios'))

@app.route('/cadastro/anuncio')
def cadastrar_anuncio():
    return render_template('cadastro_anuncio.html')

@app.route("/anuncio/novo", methods=['POST'])
def novo_anuncio():
    anuncio = Anuncio(
        request.form.get('nome'),
        request.form.get('desc'),
        request.form.get('qtd'),
        request.form.get('preco'),
        request.form.get('cat'),
        request.form.get('usu')
    )
    db.session.add(anuncio)
    db.session.commit()
    return redirect(url_for('cadastrar_anuncio'))

@app.route('/perguntas')
def perguntas():
    return render_template('perguntas.html')

@app.route('/compra')
def compra():
    print('Anúncio de compra')
    return ''

@app.route('/favoritos')
def favoritos():
    print('Inserido aos favoritos')
    return ''

@app.route('/cadastro/categoria')
def cadastro_categoria():
    return render_template('cadastro_categoria.html', categorias=Categoria.query.all(), titulo='Categorias')

@app.route('/categoria/novo', methods=['POST'])
def cadastrar_categoria():
    categoria = Categoria(request.form.get('cat'))
    db.session.add(categoria)
    db.session.commit()
    return redirect(url_for('cadastro_categoria'))

@app.route('/relatorio/venda')
def relatorio_venda():
    return render_template('relatorio_venda.html')

@app.route('/relatorio/compra')
def relatorio_compra():
    return render_template('relatorio_compra.html')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)