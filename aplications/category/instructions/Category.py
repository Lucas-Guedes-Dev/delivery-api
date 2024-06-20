from flask import jsonify
from aplications import db
from aplications.category.models import Category


class ICategory():

    def get_category(self, identifier):
        category = None
        if isinstance(identifier, int):
            category = Category.query.filter_by(id=identifier).first()
        else:
            category = Category.query.filter_by(name=identifier).first()
        
        if category is None:
            return jsonify({"error": "Categoria não encontrada"}), 404
        
        return jsonify({"id": category.id, "name": category.name}), 200

    def get_all_category(self):
        return Category.query.all()
    
    def update_category(self, id, name):
        existing_category = Category.query.filter_by(id=id).first()
        if not existing_category:
            return jsonify({"error": "Categoria não encontrada"}), 404

        # Verifica se já existe outra categoria com o mesmo nome
        category_with_same_name = Category.query.filter(Category.name == name, Category.id != id).first()
        if category_with_same_name:
            return jsonify({"error": "Já existe uma categoria com esse nome"}), 400
        
        existing_category.name = name
        db.session.commit()

        return jsonify({"message": "Categoria atualizada com sucesso", "id": existing_category.id}), 200
    
    def create_category(self, name):
        # Verifica se já existe uma categoria com o mesmo nome
        existing_category = Category.query.filter_by(name=name).first()
        if existing_category:
            return jsonify({"error": "Já existe uma categoria com esse nome "}), 400

        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()

        return jsonify({"message": "Categoria criada com sucesso", "id": new_category.id}), 201

    def delete_category(self, id):
        category = Category.query.get(id)
        if category is None:
            return jsonify({"error": "Categoria não encontrada"}), 404

        db.session.delete(category)
        db.session.commit()
        
        return jsonify({"message": "Categoria deletada com sucesso"}), 200