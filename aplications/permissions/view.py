from flask import jsonify, request
from flask.views import MethodView
from aplications.permissions.models import Permissions
from aplications.permissions.controllers.create_permission import CreatePermission
from aplications.permissions.controllers.get_permission import GetPermissions

class Permissions(MethodView):
    def getId(self, id):
        print(id)
        get_perm = GetPermissions()
        get_perm.get_id(id)
        return jsonify({'message': 'temos uma rota'}), 200
    
    def getAll(self):
        return jsonify({'message': 'temos uma rota'}), 200

    def create(self):
        json_obj = request.get_json()
        perm_obj = Permissions()
        perm_obj.name = json_obj['name']

        try:    
            # Exemplo que instacia fora de variavel pois não tem retorno
            CreatePermission().create(perm_obj)
            return jsonify({'message': 'permissão criada com sucesso'}), 200
        except Exception as e:
            return jsonify({'error': str(e)})
        
        
        