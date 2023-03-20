from app import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean, Text
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
    user = relationship("User", backref="addresses")

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
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    addresses = relationship("Address",
                              backref="user",
                              cascade="all, delete-orphan")
    
class MenuItem(db.Model):
    """menu item model"""
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(50), nullable=True)
    price = Column(Float, nullable=False, default=0)
    foods = Column(String(50), nullable=False)
    is_available = Column(Boolean, nullable=False)
    is_deliverable = Column(Boolean, nullable=False)
    duration_of_preparation = Column(DateTime)
    menu_id = Column(Integer, ForeignKey('menu.id'), nullable=False)
    created_at = Column(DateTime, nullable=False,
                          default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)

class Menu(db.Model):
    """menu model"""
    menu_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(50))
    items = db.relationship('MenuItem', backref='menu', lazy=True)
    created_at = Column(DateTime, nullable=False,
                          default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)
    restaurant = relationship('Restaurant', back_populates='menus')

class OrderItem(db.Model):
    """OrderItem model"""
    id = Column(Integer, primary_key=True)

class Order(db.Model):
    """order model"""
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    items = Column(String(500), nullable=False)
    total_price = Column(Float, nullable=False)
    address = Column(String(500), nullable=False)
    shipment_method = Column(String(50), nullable=False)
    payment_method = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    notes = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    restaurant = relationship('Restaurant', backref='orders', lazy=True)
    user = relationship('User', backref='orders', lazy=True)

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
    description = Column(String(200), nullable=True)
    duration = Column(DateTime, nullable=True)
    start = Column(DateTime, nullable=True)
    end = Column(DateTime, nullable=True)
    nb_of_person = Column(Integer, nullable=False, default=0)
    additional_info = Column(String(200), nullable=True)
    tables = Column(Integer, nullable=True)
    category = Column(String(50), nullable=True)
    price = Column(Float, nullable=False, default=0)
    tax = Column(Float, nullable=True)
    menu_item = Column(String(50), nullable=True)
    created_at = Column(DateTime, nullable=False,
                          default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
class Restaurant(db.Model):
    """Restaurant model"""
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String(50), nullable=True)
    is_operational = Column(Boolean, nullable=True)
    order_fulfilling = Column(Boolean, nullable=True)
    menus = relationship("Menu", back_populates="restaurant", cascade="all, delete-orphan")
    products = Column(String)
    orders = relationship('Orders', backref='restaurants')
    payment_methods = Column(String)
    reservations = relationship('Reservations', backref='restaurants')
    customers = Column(Integer, nullable=False, default=0)
    shipments = relationship('Shipments', backref='restaurants')
    offers = Column(String(50))
    suppliers = Column(String(50))
    created_at = Column(DateTime, nullable=False,
                          default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
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
    id = Column(Integer, primary_key=True)

class Event(db.Model):
    """Event model"""
    id = Column(Integer, primary_key=True)
    
class EventItem(db.Model):
    """EventItem model"""
    id = Column(Integer, primary_key=True)
