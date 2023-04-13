"""user model"""

from datetime import datetime

from api.core.base import declarative_base as db

class User(db.Model):
    """Users database model"""
    __tablename__ = 'users'

    id = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    salt = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=True, default='customer')
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    phone_number = db.Column(db.String(50), nullable=False)
    is_verified = db.Column(db.Boolean, nullable=False, default=False)
    password_reset_token = db.Column(db.String(255), nullable=True)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)

    payment_methods = db.relationship('PaymentMethod', backref='user', lazy=True)
    restaurants = db.relationship('Restaurant', backref='manager')
    orders = db.relationship("Order", backref="users")
    reservations = db.relationship('Reservation', backref='users')

    # Define many-to-many relationship with Address model
    addresses = db.relationship("Address",
                                secondary="users_addresses",
                                back_populates="users")

    # json serialization

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role,
            'created_at': self.created_at,
            'phone_number': self.phone_number,
            'is_verified': self.is_verified,
            'password_reset_token': self.password_reset_token,
            'updated_at': self.updated_at,
            'payment_methods': [payment_method.serialize
                                for payment_method in self.payment_methods],
            'orders': [order.serialize for order in self.orders],
            'reservations': [reservation.serialize for reservation in self.reservations],
            'restaurants': [restaurant.serialize for restaurant in self.restaurants],
            'addresses': [address.serialize for address in self.addresses],
        }