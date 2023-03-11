from app import db

class Product(db.Model):
    """
    Initialize a Menu instance
    """
    id = db.Column(db.Integer, primary_key=True)
    short_name = db.Column(db.String(50), nullable=False)
    long_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    menu_category = db.Column(db.String(50))
    menu_item = db.Column(db.String(50))
    owner = db.Column(db.String(50))
    price = db.Column(db.Integer, nullable=False)
    varients = db.Column(db.String(50))
    is_available = db.Column(db.Boolean, nullable=False)
    is_deliverable = db.Column(db.Boolean, nullable=False)
    duration_of_preparation = db.Column(db.DateTime)
    max_quantity = db.Column(db.Integer)
    # location = db.Column(db.String(50))