from flask import jsonify
from instructions import IProduct

class GetProducts(IProduct):  
    def get_product(self, identifier):
        return super().get_product(identifier)

    def get_all_product(self):
        return jsonify([{"id": product.id, "name": product.name} for product in super().get_all_product()]), 200
    
    def update_product(self, id, name) : 
        return super().update_product(id)

    def create_product(self, name):
        return super().create_product(name)

    def delete_product(self, id):
        return super().delete_product(id)
