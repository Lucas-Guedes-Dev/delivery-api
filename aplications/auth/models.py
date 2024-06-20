from aplications import db

class Auth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    phone = db.Column(db.String(18), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_profile = db.Column(db.String(256), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<User {self.username}>'