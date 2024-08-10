from flask import Flask,make_response
from markupsafe import escape
from flask import render_template
from flask import request
	app = Flask(__name__)
	@app.route("/")
	def index():
		return render_template('index.html')
	@app.route('/cadastro/usuario')
	def usuario():
		return render_template('cadastroUsuario.html',titulo="Cadastro deusuarios")
	@app.route('/cadastro/anuncio')
	def ads():
		return render_template('ads.html')
	@app.route('/ads/pergunta')
	def pergunta():
		return render_template('perguntas.html')
	@app.route('/ads/compra')
	def compra():
		print 'Anuncio de compra'
		return ''
	@app.route('/ads/favoritos')
	def favoritos():
		print 'Inserido aos favoritos'
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
	@app.route("/cadastro/cadastroUsuaio",methods=['POST'])
	def cad():
		return request.form
