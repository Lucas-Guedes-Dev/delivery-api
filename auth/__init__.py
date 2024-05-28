from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from . import routes, models

def create_auth_app():
    return auth_bp