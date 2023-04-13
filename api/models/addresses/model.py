""" addresses model"""

from datetime import datetime

from api.core.base import declarative_base as db


class Address(db.Model):
    """Addresses database model"""
    __tablename__ = 'addresses'

    id = db.Column(db.String(50), primary_key=True)
    address_one = db.Column(db.String(50), nullable=False)
    address_two = db.Column(db.String(50), nullable=True)
    phone_number = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    city_area = db.Column(db.String(50), nullable=True)
    country = db.Column(db.String(50), nullable=False)
    country_area = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(),
                           onupdate=datetime.utcnow())

    # Define many-to-many relationship with User model
    users = db.relationship("User",
                            secondary="users_addresses",
                            back_populates="addresses")

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'address_one': self.address_one,
            'address_two': self.address_two,
            'phone_number': self.phone_number,
            'city': self.city,
            'city_area': self.city_area,
            'country': self.country,
            'country_area': self.country_area,
            'users': [user.serialize for user in self.users]
        }


class UserAddress(db.Model):
    """Association table for many-to-many relationship"""
    __tablename__ = 'users_addresses'

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id'))
    address_id = db.Column(db.String(50), db.ForeignKey('addresses.id'))

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'address_id': self.address_id
        }
