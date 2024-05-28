from flask import Blueprint
from auth.view.auth import Auth
from auth import auth_bp  

auth_bp.add_url_rule('/', view_func=Auth.as_view('index'))
auth_bp.add_url_rule('/teste', view_func=Auth.as_view('view'))