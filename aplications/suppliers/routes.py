from flask import Blueprint
from aplications.suppliers.view import supplier

supplier_bp = Blueprint('supplier', __name__)

supplier_view = supplier.as_view('supplier_api')
supplier_bp.add_url_rule('/', view_func=supplier_view, methods=['GET'])
supplier_bp.add_url_rule('/<int:id>', view_func=supplier_view, methods=['GET'])
supplier_bp.add_url_rule('/create', view_func=supplier_view, methods=['POST'])
supplier_bp.add_url_rule('/update/<int:id>', view_func=supplier_view, methods=['PATCH'])
supplier_bp.add_url_rule('/delete/<int:id>', view_func=supplier_view, methods=['DELETE'])