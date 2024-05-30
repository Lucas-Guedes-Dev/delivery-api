from flask import jsonify, request
from flask.views import MethodView

class Permissions(MethodView):
    def get(self):
        return jsonify({'message': 'temos uma rota'}), 200
