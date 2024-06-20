from aplications import db

class Permissions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False, nullable=False)

    def __repr__(self):
        return f'<Permissions {self.name}>'
