from __main__ import db

class User(db.Model):
    """
    Initialize a Menu instance
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    permissions = db.Column(db.String, nullable=False)
    avatar = db.Column(db.String(20), nullable=False, default='default.jpg')
    orders = db.relationship('Order', backref='user', lazy=True)
    reservations = db.relationship('Reservation', backref='user')
    payment_methods = db.Column(db.String)
    reviews = db.Column(db.String)