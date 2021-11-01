#restful é um serviço web que segue a arquitetura rest;arquitetura padrão para construir API
from flask import Flask
from flask.globals import request
from flask_restful import Resource, Api
import json



app = Flask(__name__)
api = Api(app)
developers = [{
    'id':0,
    'nome':'Marcus',
    'skills':'Python'
    }]

class Developer(Resource):
    def get(self, id):
        """
        send a json
        """
        try:
            response = developers[id]
        except IndexError:
            msg = f'Developer with id: {id} not exist'
            response = {'status': 'Error', 'mensagem':msg}
        else:
            return response

    def put(self, id):
        return 'put'
    
    def post(self, id):
        data = json.loads(request.data)
        developers[id] = data
        return data
    
    def delete(self, id):
        """
        delete json
        """
        developers.pop(id)
        return {'dados-status':'apagados'}


class ListaDeveloper(Resource):
    """
     Insere dados através do post e retorna a lista json completa com o método HTTP get.
    """
    def post(self):
        dados = json.loads(request.data)
        developers.append(dados)
        return {'status': 'Sucesso!Registro inserido'}

    # consultar todos os dev
    def get(self):
        return developers


# mapa de rotas:
api.add_resource(Developer, '/dev/<int:id>/')
api.add_resource(ListaDeveloper, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)