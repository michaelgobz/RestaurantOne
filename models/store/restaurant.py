from app import db

class Restaurant(db.Model):
# Representation of a restaurant

    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(50), nullable=True)
    mission_statement = db.Column(db.String(50), nullable=True)
    is_operational = db.Column(db.Boolean, nullable=True)
    order_fulfilling = db.Column(db.Boolean, nullable=True)
    menus = db.relationship('Menu', backref='restaurant', lazy=True)
    products = db.Column(db.String)
    orders = db.relationship('Order', backref='restaurant', lazy=True)
    payment_methods = db.Column(db.String)
    reservations = db.relationship('Reservation', backref='restaurant', lazy=True)
    customers = db.Column(db.Integer, nullable=False, default=0)
    shipments = db.relationship('Shipment', backref='restaurant', lazy=True)
    offers = db.Column(db.String(50))
    suppliers = db.Column(db.String(50))