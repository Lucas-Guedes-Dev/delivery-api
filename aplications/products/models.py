from datetime import datetime
from aplications import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    cost_price = db.Column(db.Float)
    sku = db.Column(db.String(64), unique=True, nullable=False)
    barcode = db.Column(db.String(64), unique=True)
    brand = db.Column(db.String(64))
    manufacturer = db.Column(db.String(128))
    quantity_in_stock = db.Column(db.Integer)
    quantity_sold = db.Column(db.Integer, default=0)
    warranty = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('products', lazy=True))
    images = db.relationship('ProductImage', backref='product', lazy=True)
    specifications = db.relationship('ProductSpecification', backref='product', lazy=True)
    reviews = db.relationship('ProductReview', backref='product', lazy=True)
    
    def __repr__(self):
        return f'<Product {self.name}>'

class ProductImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    url = db.Column(db.String(255), nullable=False)

class ProductSpecification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    key = db.Column(db.String(128), nullable=False)
    value = db.Column(db.String(255), nullable=False)

class ProductReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    rating = db.Column(db.Integer)
    review_text = db.Column(db.Text)
    reviewer_name = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)