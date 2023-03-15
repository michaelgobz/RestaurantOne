""" address model"""
from ..core.base import declarative_base as db


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
