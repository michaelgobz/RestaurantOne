""" address model"""
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from ..core.base import declarative_base as db
from .user import User




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
