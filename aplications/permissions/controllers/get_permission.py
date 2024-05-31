from aplications import db
from aplications.permissions.models import Permissions
from flask import jsonify

class GetPermissions:
    def __init__(self):
        self.olamundo = "tetadecavalo"
    def get_id(self, id):
        return jsonify({
            id : id
        }),200