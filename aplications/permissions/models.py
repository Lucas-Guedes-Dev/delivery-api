from aplications import db

permissions_users = db.Table(
    'permissions_users',
    db.Column('permission_id', db.Integer, db.ForeignKey('permissions.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class PermissionsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False, nullable=False)

    def __repr__(self):
        return f'<PermissionsModel {self.name}>'
