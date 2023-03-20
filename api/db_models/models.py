
"""data models that the api uses"""
from email.policy import default
from typing import List
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import relationship

class Address(db.Model):
    """"address model object"""

    id = db.Column(db.Integer, primary_key=True)
    address_one = db.Column(db.String(50), nullable=False)
    address_two = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    city_area = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    country_area = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", backref="addresses")


class User(db.Model):
    """User model"""
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False,
                          default=datetime.utcnow)

    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    addresses =db.relationship("Address",

                              backref="user",
                              cascade="all, delete-orphan")
    
class MenuItem(db.Model):
    """menu item model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float, nullable=False, default=0)
    foods = db.Column(db.String(50), nullable=False)
    is_available = db.Column(db.Boolean, nullable=False)
    is_deliverable = db.Column(db.Boolean, nullable=False)
    duration_of_preparation = db.Column(db.DateTime)
    menu_id = db.Column(db.Integer, db.ForeignKey(
        'menu.menu_id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                          default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)

class Menu(db.Model):
    """menu model"""

    menu_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50))
    items = db.relationship('MenuItem', backref='menu', lazy=True)
    created_at = db.Column(db.DateTime, nullable=False,
                          default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'),
                              nullable=False)
    restaurant = db.relationship('Restaurant', back_populates='menus')

class OrderItem(db.Model):
    """OrderItem model"""
    id = db.Column(db.Integer, primary_key=True)

class Order(db.Model):
    """order model"""
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    items = db.Column(db.String(500), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(500), nullable=False)
    shipment_method = db.Column(db.String(50), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    restaurant = db.relationship('Restaurant', backref='orders', lazy=True)
    user = db.relationship('User', backref='orders', lazy=True)

class PaymentMethod(db.Model):
    """PaymentMethod model"""
    id = Column(Integer, primary_key=True)
    
class Payment(db.Model):
    """Payment model"""
    id = Column(Integer, primary_key=True)
    
class TransactionItem(db.Model):
    """TransactionItem model"""
    id = Column(Integer, primary_key=True)
    

class Transaction(db.Model):
    """Transaction model"""
    id = Column(Integer, primary_key=True)
    
class ReservationItem(db.Model):
    """Reservation Item model"""
    id = Column(Integer, primary_key=True)
    
class Reservation(db.Model):
    """Reservation model"""
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=True)
    duration = db.Column(db.DateTime, nullable=True)
    start = db.Column(db.DateTime, nullable=True)
    end = db.Column(db.DateTime, nullable=True)
    nb_of_person = db.Column(db.Integer, nullable=False, default=0)
    additional_info = db.Column(db.String(200), nullable=True)
    tables = db.Column(db.Integer, nullable=True)
    category = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float, nullable=False, default=0)
    tax = db.Column(db.Float, nullable=True)
    menu_item = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                          default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
class Restaurant(db.Model):
    """Restaurant model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(50), nullable=True)
    is_operational = db.Column(db.Boolean, nullable=True)
    order_fulfilling = db.Column(db.Boolean, nullable=True)
    menus = db.relationship("Menu", back_populates="restaurant",
                            cascade="all, delete-orphan")
    products = db.Column(db.String)
    orders = db.relationship('Orders', backref='restaurants')
    payment_methods = db.Column(db.String)
    reservations = db.relationship('Reservations', backref='restaurant')
    customers = db.Column(db.Integer, nullable=False, default=0)
    shipments = db.relationship('Shipments', backref='restaurants')
    offers = db.Column(db.String(50))
    suppliers = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, nullable=False,
                          default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,

                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    
class ShipmentMethod(db.Model):
    """Shipment method model"""
    id = Column(Integer, primary_key=True)
    

class Shipment(db.Model):
    """Shipment model"""
    id = Column(Integer, primary_key=True)
    

class Invoice(db.Model):
    """ Invoice model"""
    id = Column(Integer, primary_key=True)
    
class InvoiceItem(db.Model):
    """InvoiceItem model"""
    id = Column(Integer, primary_key=True)
    
class Information(db.Model):
    """information model"""
    id = Column(Integer, primary_key=True)
    
class Review(db.Model):
    """Review model"""
    id = Column(Integer, primary_key=True)
    
class ReviewItem(db.Model):

    """ReviewItem model"""
    id = db.Column(db.Integer, primary_key=True)

class Event(db.Model):
    """Event model"""
    id = Column(Integer, primary_key=True)
    
class EventItem(db.Model):
    """EventItem model"""

    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(50), default="", nullable=True)

