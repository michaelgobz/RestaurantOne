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
            'Id': self.id,
            'Email': self.email,
            'FirstName': self.first_name,
            'LastName': self.last_name,
            'Role': self.role,
            'CreatedAt': self.created_at,
            'PhoneNumber': self.phone_number,
            'IsVerified': self.is_verified,
            # TODO: this token should be in a redis cache in version 2.1
            'PasswordResetToken': self.password_reset_token,
            'UpdatedAt': self.updated_at,
            'PaymentMethods': [payment_method.serialize
                                for payment_method in self.payment_methods],
            'Orders': [order.serialize for order in self.orders],
            'Reservations': [reservation.serialize for reservation in self.reservations],
            'Restaurants': [restaurant.serialize for restaurant in self.restaurants],
            'Addresses': [address.serialize for address in self.addresses],
        }