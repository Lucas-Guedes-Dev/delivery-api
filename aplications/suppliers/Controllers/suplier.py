from flask import jsonify
from instructions import ISupplier

class GetSupplier(ISupplier):  
    def get_supplier(self, identifier):
        return super().get_supplier(identifier)

    def get_all_supplier(self):
        return jsonify([{"id": supplier.id, "name": supplier.name} for supplier in super().get_all_supplier()]), 200
    
    def update_supplier(self, id, name) : 
        return super().update_supplier(id)

    def create_supplier(self, name):
        return super().create_supplier(name)

    def delete_supplier(self, id):
        return super().delete_supplier(id)
