from flask import jsonify, request
from flask.views import MethodView

class Auth(MethodView):
    def get(self):
        return jsonify({'message': 'temos uma rota'}), 200
    
    def get_id(self, id=None):
        return jsonify({'message': f'chegou no get com id {id}'}), 200
    
    def post(self):
        data = request.get_json()
        return jsonify({'message': 'POST request received', 'data': data}), 201

    def patch(self, id):
        if not id:
            return jsonify({'error': 'ID is required for PATCH'}), 400
        data = request.get_json()
        return jsonify({'message': f'PATCH request received for ID {id}', 'data': data}), 200

    def delete(self, id):
        if not id:
            return jsonify({'error': 'ID is required for DELETE'}), 400
        return jsonify({'message': f'DELETE request received for ID {id}'}), 204
