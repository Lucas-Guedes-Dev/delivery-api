from flask import jsonify
from aplications import db
from aplications.suppliers.Controllers import Supplier


class ISupplier():

    def get_Supplier(self, identifier):
        Supplier = None
        if isinstance(identifier, int):
            Supplier = Supplier.query.filter_by(id=identifier).first()
        else:
            Supplier = Supplier.query.filter_by(name=identifier).first()
        
        if Supplier is None:
            return jsonify({"error": "Fornecedor não encontrado"}), 404
        
        return jsonify({"id": Supplier.id, "name": Supplier.name}), 200

    def get_all_Supplier(self):
        return Supplier.query.all()
    
    def update_Supplier(self, id, name):
        existing_Supplier = Supplier.query.filter_by(id=id).first()
        if not existing_Supplier:
            return jsonify({"error": "Fornecedor não encontrado"}), 404

        # Verifica se já existe outra Fornecedor com o mesmo nome
        Supplier_with_same_name = Supplier.query.filter(Supplier.name == name, Supplier.id != id).first()
        if Supplier_with_same_name:
            return jsonify({"error": "Já existe uma Fornecedor com esse nome"}), 400
        
        existing_Supplier.name = name
        db.session.commit()

        return jsonify({"message": "Fornecedor atualizada com sucesso", "id": existing_Supplier.id}), 200
    
    def create_Supplier(self, name):
        # Verifica se já existe uma Fornecedor com o mesmo nome
        existing_Supplier = Supplier.query.filter_by(name=name).first()
        if existing_Supplier:
            return jsonify({"error": "Já existe uma Fornecedor com esse nome "}), 400

        new_Supplier = Supplier(name=name)
        db.session.add(new_Supplier)
        db.session.commit()

        return jsonify({"message": "Fornecedor registrado com sucesso", "id": new_Supplier.id}), 201

    def delete_Supplier(self, id):
        Supplier = Supplier.query.get(id)
        if Supplier is None:
            return jsonify({"error": "Fornecedor não encontrado"}), 404

        db.session.delete(Supplier)
        db.session.commit()
        
        return jsonify({"message": "Fornecedor deletado com sucesso"}), 200