from app import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Address(db.Model):
    """"address model object"""
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    address_one = Column(String(50), nullable=False)
    address_two = Column(String(50), nullable=False)
    phone_number = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    city_area = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    country_area = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates="addresses")

class User(db.Model):
    """User model"""
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False,
                          default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                           default=datetime.utcnow)
    addresses = relationship("Address",
                              back_populates="user",
                              cascade="all, delete-orphan")
    
class MenuItem(db.Model):
    """menu item model"""
    id = Column(Integer, primary_key=True)

class Menu(db.Model):
    """menu model"""
    id = Column(Integer, primary_key=True)

class OrderItem(db.Model):
    """OrderItem model"""
    id = Column(Integer, primary_key=True)
    
class Order(db.Model):
    """Order model"""
    id = Column(Integer, primary_key=True)
    
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
    id = Column(Integer, primary_key=True)
    
class Restaurant(db.Model):
    """Restaurant model"""
    id = Column(Integer, primary_key=True)
    
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
    id = Column(Integer, primary_key=True)

class Event(db.Model):
    """Event model"""
    id = Column(Integer, primary_key=True)
    
class EventItem(db.Model):
    """EventItem model"""
    id = Column(Integer, primary_key=True)
