from flask import Blueprint
from aplications.permissions.view import Permissions

permission_bp = Blueprint('permissions', __name__)

permission_bp.add_url_rule('/', view_func=Permissions.as_view("permissions_getAll"), methods=['GET'])
permission_bp.add_url_rule('/selectPermission/<int:id>', view_func=Permissions.as_view("permissions_getId"), methods=['GET'])
permission_bp.add_url_rule('/create', view_func=Permissions.as_view("permissions_create"), methods=['POST'])
