from flask import jsonify, request
from flask.views import MethodView

class Auth(MethodView):
    def get(self, id=None):
        if id:
            return jsonify({'message': 'chegou o id'}), 200
        else:
            return jsonify({'message': 'Status 200k chegou com sucesso'}), 200

    # Métodos adicionais
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