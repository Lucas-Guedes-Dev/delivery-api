from flask import Blueprint
from aplications.products.view import product

product_bp = Blueprint('product', __name__)

category_view = category.as_view('category_api')
product_bp.add_url_rule('/', view_func=category_view, methods=['GET'])
product_bp.add_url_rule('/<int:id>', view_func=category_view, methods=['GET'])
product_bp.add_url_rule('/create', view_func=category_view, methods=['POST'])
product_bp.add_url_rule('/update/<int:id>', view_func=category_view, methods=['PATCH'])
product_bp.add_url_rule('/delete/<int:id>', view_func=category_view, methods=['DELETE'])