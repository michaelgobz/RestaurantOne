from app import db

class Order(db.Model):
    """
    Initialize a Menu instance
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items = db.Column(db.String(50))
    total_cart_price = db.Column(db.Integer, nullable=False)
    address = db.Column(db.Text)
    shipment_method = db.Column(db.String(50))
    payment_method = db.Column(db.String(50))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)