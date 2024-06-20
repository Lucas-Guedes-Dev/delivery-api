from flask import Blueprint
from aplications.category.view import category

category_bp = Blueprint('category', __name__)

category_view = category.as_view('category_api')
category_bp.add_url_rule('/', view_func=category_view, methods=['GET'])
category_bp.add_url_rule('/<int:id>', view_func=category_view, methods=['GET'])
category_bp.add_url_rule('/create', view_func=category_view, methods=['POST'])
category_bp.add_url_rule('/update/<int:id>', view_func=category_view, methods=['PATCH'])
category_bp.add_url_rule('/delete/<int:id>', view_func=category_view, methods=['DELETE'])