from flask import jsonify
from instructions import ICategory

class GetCategories(ICategory):  
    def get_category(self, identifier):
        return super().get_category(identifier)

    def get_all_category(self):
        return jsonify([{"id": category.id, "name": category.name} for category in super().get_all_category()]), 200
    
    def update_category(self, id, name) : 
        return super().update_category(id)

    def create_category(self, name):
        return super().create_category(name)

    def delete_category(self, id):
        return super().delete_category(id)
