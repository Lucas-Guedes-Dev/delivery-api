from flask import jsonify, request
from flask.views import MethodView
from category.Controllers.Get_categories import GetCategories

class Category(MethodView):
    def get(self, identifier=None):
        if identifier:
            return GetCategories().get_category(identifier)
        else:
            return GetCategories().get_all_category()

    def post(self):
        data = request.get_json()
        name = data.get('name')
        return GetCategories().create_category(name)

    def patch(self, id):
        data = request.get_json()
        name = data.get('name')
        return GetCategories().update_category(id, name)

    def delete(self, id):
        if not id:
            return jsonify({'error': 'ID is required for DELETE'}), 400
        
        return GetCategories().delete_category(id)
