from flask import jsonify, request
from flask.views import MethodView
from aplications.permissions.models import Permissions
from aplications.permissions.controllers.create_permission import CreatePermission

class Permissions(MethodView):
    def get(self):
        return jsonify({'message': 'temos uma rota'}), 200

    def post(self):
        json_obj = request.get_json()
        perm_obj = Permissions()
        perm_obj.name = json_obj['name']

        try:    
            CreatePermission().create(perm_obj)
            return jsonify({'message': 'permissão criada com sucesso'}), 200
        except Exception as e:
            return jsonify({'error': str(e)})
        
        
        