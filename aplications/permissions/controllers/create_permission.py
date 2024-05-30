from aplications import db
from aplications.permissions.models import Permissions

class CreatePermission():
    def create(self, perm_obj: Permissions):
        new_register = Permissions(name=perm_obj.name)
    
        db.session.add(new_register)
        db.session.commit()