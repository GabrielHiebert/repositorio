from config import * 
from perfil import Perfil 
 
@app.route("/") 
def inicio(): 
   return 'Sistema de cadastro de usuarios. '+\
         '<a href="/listar_usuarios">Operação listar</a>'

@app.route("/listar_usuarios") 
def listar_usuarios(): 
   # obter os ususários do cadastro 
   usuarios = db.session.query(Perfil).all() 
   # aplicar o método json que a classe Perfil possui a cada elemento da lista 
   usuarios_em_json = [ x.json() for x in usuarios ] 
   # converter a lista do python para json 
   resposta = jsonify(usuarios_em_json)
   #permitir resposta para outros pedidos oriundos de outras tecnologias
   resposta.headers.add("Access-Control-Allow-Origin", "*")
   return resposta #retornar...

app.run(debug=True) 
