from aplications import db

permissions_auth = db.Table(
    'permissions_auth',
    db.Column('permission_id', db.Integer, db.ForeignKey('permissions.id'), primary_key=True),
    db.Column('Auth_id', db.Integer, db.ForeignKey('Auth.id'), primary_key=True)
)