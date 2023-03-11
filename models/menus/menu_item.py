from app import db

class MenuItem(db.Model):
#   Representation of a menu item

    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Integer, nullable=False, default=0)
    foods = db.Column(db.String(50), nullable=False)
    toppings = db.Column(db.String(50), nullable=True)
    serving_model = db.Column(db.String(50), nullable=True)
    tax_associated = db.Column(db.Integer, nullable=True)