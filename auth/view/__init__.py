from flask import jsonify, request
from flask.views import MethodView
from .docs import get_docs, get_id_docs, post_docs, patch_docs, delete_docs

class Auth(MethodView):
    @get_docs()
    def get(self):
        return jsonify({'message': 'temos uma rota'}), 200
    
    @get_id_docs()
    def get_id(self, id=None):
        return jsonify({'message': f'chegou no get com id {id}'}), 200
    
    @post_docs()
    def post(self):
        data = request.get_json()
        return jsonify({'message': 'POST request received', 'data': data}), 201

    @patch_docs()
    def patch(self, id):
        if not id:
            return jsonify({'error': 'ID is required for PATCH'}), 400
        data = request.get_json()
        return jsonify({'message': f'PATCH request received for ID {id}', 'data': data}), 200

    @delete_docs()
    def delete(self, id):
        if not id:
            return jsonify({'error': 'ID is required for DELETE'}), 400
        return jsonify({'message': f'DELETE request received for ID {id}'}), 204
