from flask import Blueprint
from aplications.permissions.view import Permissions

permission_bp = Blueprint('permissions', __name__)

permission_view = Permissions.as_view('permission_api')
permission_bp.add_url_rule('/', view_func=permission_view, methods=['GET'])
permission_bp.add_url_rule('/id/<int:id>', view_func=permission_view, methods=['GET'])
permission_bp.add_url_rule('/create', view_func=permission_view, methods=['POST'])
