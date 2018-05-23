from bottle import route, run
from bottle import request, template
from bottle import static_file, get
from bottle import error

'''@route('/')
@route('/user/<nome>')
def index(nome='null'):
	return '<center><h1>Eae ' + nome + ' </h1></center>'

@route('/artigo/<id>')
def index_artigo(id):
	return '<h2>Você está lendo o artigo ' + id + '</h2>'

@route('/pagina/<id>/<nome>')
def index_pagina(id, nome):
	return '<h1>Você está lendo a página ' + id + ' com o nome ' + nome + '</h1>'
'''

# static rotes
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='static/css')

@get('/<filename:re:.*\.css')
def stylesheets(filename):
	return static_file(filename, root='static/js')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def stylesheets(filename):
	return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def stylesheets(filename):
	return static(filename, root='static/fonts')

@route('/login') # @get('/login')
def login():
	return template('login')

def auth_login(username, password):
	dic = {'igo.barros': '123', 'dina.pereira': '1234', 'afonso.barros': '12345', 'maria.luana': '123456'}
	#return True if dic[username] == password else False
	if username in dic.keys() and dic[username] == password:
		return True
	return False 


@route('/login', method='POST')
def acao_login(): # @post('/login')
	username = request.forms.get('username')
	password = request.forms.get('password')
	sucesso = auth_login(username, password)
	return template('verificacao_login', sucesso=sucesso, nome=username) # ou sucesso=auth_login(username, password)

@error(404)
def error404(error):
	return template('pagina404')

if __name__ == '__main__':
	run(host='localhost', port=8080, debug=True, reloader=True)