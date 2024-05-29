from flask import Blueprint, Flask, request
from flask.views import MethodView

# Definir o Blueprint
auth_bp = Blueprint('auth', __name__)

# Definir a classe Auth com métodos HTTP específicos
class Auth(MethodView):
    def get(self):
        return "GET request received", 200

    def post(self):
        data = request.get_json()
        return {"message": "POST request received", "data": data}, 201

    def patch(self):
        data = request.get_json()
        return {"message": "PATCH request received", "data": data}, 200

    def delete(self):
        return {"message": "DELETE request received"}, 204

# Criar a aplicação Flask
app = Flask(__name__)

# Registrar a view com o Blueprint para diferentes métodos HTTP
auth_bp.add_url_rule('/auth/', view_func=Auth.as_view('auth_index'), methods=['GET'])
auth_bp.add_url_rule('/auth/<int:id>', view_func=Auth.as_view('auth_index'), methods=['GET'])
auth_bp.add_url_rule('/auth/create', view_func=Auth.as_view('auth_post'), methods=['POST'])
auth_bp.add_url_rule('/auth/update/<int:id>', view_func=Auth.as_view('auth_patch'), methods=['PATCH'])
auth_bp.add_url_rule('/auth/delete/<int:id>', view_func=Auth.as_view('auth_delete'), methods=['DELETE'])

# Registrar o Blueprint com a aplicação Flask
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)