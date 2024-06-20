from flask import jsonify
from aplications import db
from aplications.products.models import Product


class IProduct():

    def get_Product(self, identifier):
        Product = None
        if isinstance(identifier, int):
            Product = Product.query.filter_by(id=identifier).first()
        else:
            Product = Product.query.filter_by(name=identifier).first()
        
        if Product is None:
            return jsonify({"error": "Produto não encontrado"}), 404
        
        return jsonify({"id": Product.id, "name": Product.name}), 200

    def get_all_Product(self):
        return Product.query.all()
    
    def update_Product(self, id, name):
        existing_Product = Product.query.filter_by(id=id).first()
        if not existing_Product:
            return jsonify({"error": "Produto não encontrado"}), 404

        # Verifica se já existe outra Produto com o mesmo nome
        Product_with_same_name = Product.query.filter(Product.name == name, Product.id != id).first()
        if Product_with_same_name:
            return jsonify({"error": "Já existe uma Produto com esse nome"}), 400
        
        existing_Product.name = name
        db.session.commit()

        return jsonify({"message": "Produto atualizada com sucesso", "id": existing_Product.id}), 200
    
    def create_Product(self, name):
        # Verifica se já existe uma Produto com o mesmo nome
        existing_Product = Product.query.filter_by(name=name).first()
        if existing_Product:
            return jsonify({"error": "Já existe uma Produto com esse nome "}), 400

        new_Product = Product(name=name)
        db.session.add(new_Product)
        db.session.commit()

        return jsonify({"message": "Produto criado com sucesso", "id": new_Product.id}), 201

    def delete_Product(self, id):
        Product = Product.query.get(id)
        if Product is None:
            return jsonify({"error": "Produto não encontrado"}), 404

        db.session.delete(Product)
        db.session.commit()
        
        return jsonify({"message": "Produto deletado com sucesso"}), 200