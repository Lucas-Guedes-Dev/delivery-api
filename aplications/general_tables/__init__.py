from aplications import db
from sqlalchemy.orm import validates
from sqlalchemy import event

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    phone = db.Column(db.String(18), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_profile = db.Column(db.String(256), nullable=True)
    document_number = db.Column(db.String(42), nullable=True)
    isAdmin = db.Column(db.Boolean, default=False)
    isClerk = db.Column(db.Boolean, default=False)
    isSupplier = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.username}>'

    @validates('isAdmin', 'isClerk', 'isSupplier')
    def validate_roles(self, key, value):
        if value:  # Só valida quando o valor é True
            if key == 'isAdmin' and (self.isClerk or self.isSupplier):
                raise ValueError("Only one role can be True at a time.")
            if key == 'isClerk' and (self.isAdmin or self.isSupplier):
                raise ValueError("Only one role can be True at a time.")
            if key == 'isSupplier' and (self.isAdmin or self.isClerk):
                raise ValueError("Only one role can be True at a time.")
        return value

@event.listens_for(Person, 'before_insert')
@event.listens_for(Person, 'before_update')
def ensure_single_role(mapper, connection, target):
    if sum([target.isAdmin, target.isClerk, target.isSupplier]) > 1:
        raise ValueError("Only one role can be True at a time.")