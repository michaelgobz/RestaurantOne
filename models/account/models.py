"""Account models."""
from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Address(db.Model):
    """"address model object"""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address_one = db.Column(db.String(50), nullable=False)
    address_two = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    city_area = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    country_area = db.Column(db.String(50), nullable=False)
    user_id:Mapped[int] = mapped_column(db.Integer, 
                                    db.ForeignKey('user.id'), nullable=False)
    user:Mapped['User'] = db.relationship("User", backref="addresses")

class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                          default=datetime.utcnow, editable=False)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow, editable=True)
    addresses: Mapped[List['Address']] = db.relationship("Address", backref="user",
                                                       cascade="all, delete-orphan")
