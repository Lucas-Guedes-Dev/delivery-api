from datetime import datetime
from aplications import db

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128))
    phone_number = db.Column(db.String(20))
    address = db.Column(db.Text)
    document_number = db.Column(db.Text)
    categorie_products = db.relationship('Categories', backref='supplier', lazy=True)
    products_supplied = db.relationship('Product', backref='supplier', lazy=True)

    def __repr__(self):
        return f'<Supplier {self.name}>'