from flask import jsonify, request
from flask.views import MethodView
from products.Controllers.Get_product import GetProducts

class Product(MethodView):
    def get(self, identifier=None):
        if identifier:
            return GetProducts().get_product(identifier)
        else:
            return GetProducts().get_all_product()

    def post(self):
        data = request.get_json()
        name = data.get('name')
        return GetProducts().create_product(name)

    def patch(self, id):
        data = request.get_json()
        name = data.get('name')
        return GetProducts().update_product(id, name)

    def delete(self, id):
        if not id:
            return jsonify({'error': 'ID is required for DELETE'}), 400
        
        return GetProducts().delete_product(id)
