from flask import Blueprint
from auth.view import Auth

auth_bp = Blueprint('auth', __name__)

auth_bp.add_url_rule('/', view_func=Auth.as_view('auth_get'), methods=['GET'])
auth_bp.add_url_rule('/<int:id>', view_func=Auth.as_view('auth_get_id'), methods=['GET'])
auth_bp.add_url_rule('/create', view_func=Auth.as_view('auth_post'), methods=['POST'])
auth_bp.add_url_rule('/update/<int:id>', view_func=Auth.as_view('auth_patch'), methods=['PATCH'])
auth_bp.add_url_rule('/delete/<int:id>', view_func=Auth.as_view('auth_delete'), methods=['DELETE'])