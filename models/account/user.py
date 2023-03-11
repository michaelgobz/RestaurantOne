from __main__ import db

class User(db.Model):
 #  Representation of a user

   __tablename__ = 'users'

   id = db.Column(db.Integer, primary_key=True)
   email = db.Column(db.String(120), unique=True, nullable=False)
   password = db.Column(db.String(60), nullable=False)
   first_name = db.Column(db.String(50), nullable=False)
   last_name = db.Column(db.String(50), nullable=False)
   phone = db.Column(db.Integer, unique=True, nullable=True)
   country = db.Column(db.String(50), nullable=True)
   location = db.Column(db.String(50), nullable=True)
   address = db.Column(db.String(150), nullable=True)
   role = db.Column(db.String(50), nullable=False)
   permissions = db.Column(db.String, nullable=False)
   avatar = db.Column(db.String(20), nullable=False, default='default.jpg')
   orders = db.relationship('Order', backref='user', lazy=True)
   reservations = db.relationship('Reservation', backref='user')
   payment_methods = db.Column(db.String, nullable=True)
   reviews = db.Column(db.String(1000), nullable=True)