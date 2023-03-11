from app import db

class Restaurant(db.Model):
    """
    Initialize a Menu instance
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    mission_statement = db.Column(db.String(50))
    is_operational = db.Column(db.Boolean, nullable=False)
    order_fulfilling = db.Column(db.Boolean, nullable=False)
    menus = db.relationship('Menu', backref='restaurant', lazy=True)
    products = db.Column(db.String)
    orders = db.relationship('Order', backref='restaurant', lazy=True)
    payment_methods = db.Column(db.String)
    reservations = db.relationship('Reservation', backref='restaurant', lazy=True)
    customers = db.Column(db.Integer, foreign_key=True)
    shipments = db.Column(db.Integer, foreign_key=True)
    offers = db.Column(db.String(50))
    suppliers = db.Column(db.String(50))