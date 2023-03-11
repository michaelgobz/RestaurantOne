from app import db

class Order(db.Model):
#    Representation of an order

    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items = db.Column(db.String(50), nullable=False)
    total_cart_price = db.Column(db.Integer, nullable=False, default=0)
    address = db.Column(db.Text, nullable=False)
    shipment_method = db.Column(db.String(50), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)