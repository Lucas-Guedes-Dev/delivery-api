# auth/services.py

from flask import jsonify, request
from flask.views import MethodView

class Auth(MethodView):
    def __init__(self):
        super().__init__()
    
    def dispatch_request(self, id=None):
        if request.method == 'GET':
            return self.get()
        elif request.method == 'POST':
            return self.post()
        elif request.method == 'PATCH':
            return self.patch(id)
        elif request.method == 'DELETE':
            return self.delete(id)
        else:
            return jsonify({'error': 'Method not allowed'}), 405

    def get(self):
        # Lógica para requisições GET
        return jsonify({'message': 'chegou no get'}), 200

    def post(self):
        # Lógica para requisições POST
        data = request.get_json()
        return jsonify({'message': 'POST request received', 'data': data}), 201

    def patch(self, id):
        # Lógica para requisições PATCH
        if not id:
            return jsonify({'error': 'ID is required for PATCH'}), 400
        data = request.get_json()
        return jsonify({'message': f'PATCH request received for ID {id}', 'data': data}), 200

    def delete(self, id):
        # Lógica para requisições DELETE
        if not id:
            return jsonify({'error': 'ID is required for DELETE'}), 400
        return jsonify({'message': f'DELETE request received for ID {id}'}), 204