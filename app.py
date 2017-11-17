from bottle import run,route,template,request
from sqlalchemy import create_engine
@route('/')
def login() :
	return template("credenciales.tpl")

@route('/conectar')
def conectar() :
	usuario=request.params.get('usuario')
	password=request.params.get('password')
	lista=[]
        db_string = "postgres://"+usuario+":"+password+"@172.22.200.182:5432/prueba"
	db = create_engine(db_string)
	lista=[]
	result_set = db.execute("SELECT * FROM ingredientes")  
	for row in result_set:
	    lista.append(dict(row))
	return template("conexion.tpl",datos=lista)
run(host='0.0.0.0',port='8080')
