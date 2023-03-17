from app import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import relationship


class Address(db.Model):
    """"address model object"""
    id = Column(Integer, primary_key=True)
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
    menu_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(50), nullable=True)
    price = Column(Integer, nullable=False, default=0)
    foods = Column(String(50), nullable=False)
    is_available = Column(Boolean, nullable=False)
    is_deliverable = Column(Boolean, nullable=False)
    duration_of_preparation = Column(DateTime)

class Menu(db.Model):
    """menu model"""
    menu_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(50))
    items = Column(String(50))
    created_at = Column(DateTime, nullable=False,
                          default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                           default=datetime.utcnow)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)

class OrderItem(db.Model):
    """OrderItem model"""
    id = Column(Integer, primary_key=True)
    
class Order(db.Model):
    """Order model"""
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    items = Column(String(50), nullable=False)
    total_cart_price = Column(Integer, nullable=False, default=0)
    address = Column(Text, nullable=False)
    shipment_method = Column(String(50), nullable=False)
    payment_method = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False,
                          default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                           default=datetime.utcnow)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    
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
    description = Column(Text, nullable=True)
    nb_of_person = Column(Integer, nullable=False, default=0)
    duration = Column(DateTime, nullable=True)
    start = Column(DateTime, nullable=True)
    end = Column(DateTime, nullable=True)
    nb_of_person = Column(Integer, nullable=False, default=0)
    additional_info = Column(Text, nullable=True)
    tables = Column(Integer, nullable=True)
    category = Column(String(50), nullable=True)
    price = Column(Integer, nullable=False, default=0)
    tax = Column(Integer, nullable=True)
    menu_item = Column(String(50), nullable=True)
    created_at = Column(DateTime, nullable=False,
                          default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                           default=datetime.utcnow)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
class Restaurant(db.Model):
    """Restaurant model"""
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String(50), nullable=True)
    is_operational = Column(Boolean, nullable=True)
    order_fulfilling = Column(Boolean, nullable=True)
    menus = relationship('Menus', back_populates='restaurant')
    products = Column(String)
    orders = relationship('Orders', back_populates='restaurant')
    payment_methods = Column(String)
    reservations = relationship('Reservations', back_populates='restaurant')
    customers = Column(Integer, nullable=False, default=0)
    shipments = relationship('Shipments', back_populates='restaurant')
    offers = Column(String(50))
    suppliers = Column(String(50))
    created_at = Column(DateTime, nullable=False,
                          default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                           default=datetime.utcnow)
    
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
