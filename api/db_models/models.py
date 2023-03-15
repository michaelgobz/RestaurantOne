"""Account models."""
from typing import List
from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
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
    user_id:Mapped[int] = mapped_column(db.Integer, 
                                    db.ForeignKey('user.id'), nullable=False)
    user: Mapped['User'] = db.relationship("User", back_populates="addresses")
    

class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                          default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    addresses: Mapped[List['Address']] = db.relationship("Address",
                                                         back_populates="user",
                                                       cascade="all, delete-orphan")
    
class MenuItem(db.Model):
    """menu item model"""
    id = db.Column(db.Integer, primary_key=True)

class Menu(db.Model):
    """menu model"""
    id = db.Column(db.Integer, primary_key=True)

class OrderItem(db.Model):
    """OrderItem model"""
    id = db.Column(db.Integer, primary_key=True)
    
class Order(db.Model):
    """Order model"""
    id = db.Column(db.Integer, primary_key=True)
    
class PaymentMethod(db.Model):
    """PaymentMethod model"""
    id = db.Column(db.Integer, primary_key=True)
    
class Payment(db.Model):
    """Payment model"""
    id = db.Column(db.Integer, primary_key=True)
    
class TransactionItem(db.Model):
    """TransactionItem model"""
    id = db.Column(db.Integer, primary_key=True)
    

class Transaction(db.Model):
    """Transaction model"""
    id = db.Column(db.Integer, primary_key=True)
    
class ReservationItem(db.Model):
    """Reservation Item model"""
    id = db.Column(db.Integer, primary_key=True)
    
class Reservation(db.Model):
    """Reservation model"""
    id = db.Column(db.Integer, primary_key=True)
    
class Restaurant(db.Model):
    """Restaurant model"""
    id = db.Column(db.Integer, primary_key=True)
    
class ShipmentMethod(db.Model):
    """Shipment method model"""
    id = db.Column(db.Integer, primary_key=True)
    

class Shipment(db.Model):
    """Shipment model"""
    id = db.Column(db.Integer, primary_key=True)
    

class Invoice(db.Model):
    """ Invoice model"""
    id = db.Column(db.Integer, primary_key=True)
    
class InvoiceItem(db.Model):
    """InvoiceItem model"""
    id = db.Column(db.Integer, primary_key=True)
    
class Information(db.Model):
    """information model"""
    id = db.Column(db.Integer, primary_key=True)
    
class Review(db.Model):
    """Review model"""
    id = db.Column(db.Integer, primary_key=True)
    
class ReviewItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Event(db.Model):
    """Event model"""
    id = db.Column(db.Integer, primary_key=True)
    
class EventItem(db.Model):
    """EventItem model"""
    id = db.Column(db.Integer, primary_key=True)
