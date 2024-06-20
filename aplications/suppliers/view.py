from flask import jsonify, request
from flask.views import MethodView
from suppliers.Controllers.suplier import GetCategories

class Supplier(MethodView):
    def get(self, identifier=None):
        if identifier:
            return GetCategories().get_Supplier(identifier)
        else:
            return GetCategories().get_all_Supplier()

    def post(self):
        data = request.get_json()
        name = data.get('name')
        return GetCategories().create_Supplier(name)

    def patch(self, id):
        data = request.get_json()
        name = data.get('name')
        return GetCategories().update_Supplier(id, name)

    def delete(self, id):
        if not id:
            return jsonify({'error': 'ID is required for DELETE'}), 400
        
        return GetCategories().delete_Supplier(id)
