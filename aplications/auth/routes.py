from flask import Blueprint
from aplications.auth.view import Auth

auth_bp = Blueprint('auth', __name__)

auth_view = Auth.as_view('auth_api')
auth_bp.add_url_rule('/', view_func=auth_view, methods=['GET'])
auth_bp.add_url_rule('/<int:id>', view_func=auth_view, methods=['GET'])
auth_bp.add_url_rule('/create', view_func=auth_view, methods=['POST'])
auth_bp.add_url_rule('/update/<int:id>', view_func=auth_view, methods=['PATCH'])
auth_bp.add_url_rule('/delete/<int:id>', view_func=auth_view, methods=['DELETE'])