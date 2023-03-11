from app import db

class Product(db.Model):
# Representation of a product

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    short_name = db.Column(db.String(50), nullable=False)
    long_name = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=False)
    menu_category = db.Column(db.String(50), nullable=True)
    menu_item = db.Column(db.String(50), nullable=True)
    owner = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Integer, nullable=False, default=0)
    varients = db.Column(db.String(50), nullable=True)
    is_available = db.Column(db.Boolean, nullable=False)
    is_deliverable = db.Column(db.Boolean, nullable=False)
    duration_of_preparation = db.Column(db.DateTime)
    max_quantity = db.Column(db.Integer, nullable=False, default=0)
    location = db.Column(db.String(50), nullable=True)