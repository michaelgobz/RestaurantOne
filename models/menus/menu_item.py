from app import db

class MenuItem(db.Model):
    """
    Creating a Menu model
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50))
    price = db.Column(db.Integer, nullable=False)
    foods = db.Column(db.String(50), nullable=False)
    toppings = db.Column(db.String(50), nullable=False)
    serving_model = db.Column(db.String(50), nullable=False)
    tax_associated = db.Column(db.Integer, nullable=False)