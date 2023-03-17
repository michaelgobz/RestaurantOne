from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Address(Base):
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

class User(Base):
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
    
class MenuItem(Base):
    """menu item model"""
    id = Column(Integer, primary_key=True)

class Menu(Base):
    """menu model"""
    id = Column(Integer, primary_key=True)

class OrderItem(Base):
    """OrderItem model"""
    id = Column(Integer, primary_key=True)
    
class Order(Base):
    """Order model"""
    id = Column(Integer, primary_key=True)
    
class PaymentMethod(Base):
    """PaymentMethod model"""
    id = Column(Integer, primary_key=True)
    
class Payment(Base):
    """Payment model"""
    id = Column(Integer, primary_key=True)
    
class TransactionItem(Base):
    """TransactionItem model"""
    id = Column(Integer, primary_key=True)
    

class Transaction(Base):
    """Transaction model"""
    id = Column(Integer, primary_key=True)
    
class ReservationItem(Base):
    """Reservation Item model"""
    id = Column(Integer, primary_key=True)
    
class Reservation(Base):
    """Reservation model"""
    id = Column(Integer, primary_key=True)
    
class Restaurant(Base):
    """Restaurant model"""
    id = Column(Integer, primary_key=True)
    
class ShipmentMethod(Base):
    """Shipment method model"""
    id = Column(Integer, primary_key=True)
    

class Shipment(Base):
    """Shipment model"""
    id = Column(Integer, primary_key=True)
    

class Invoice(Base):
    """ Invoice model"""
    id = Column(Integer, primary_key=True)
    
class InvoiceItem(Base):
    """InvoiceItem model"""
    id = Column(Integer, primary_key=True)
    
class Information(Base):
    """information model"""
    id = Column(Integer, primary_key=True)
    
class Review(Base):
    """Review model"""
    id = Column(Integer, primary_key=True)
    
class ReviewItem(Base):
    id = Column(Integer, primary_key=True)

class Event(Base):
    """Event model"""
    id = Column(Integer, primary_key=True)
    
class EventItem(Base):
    """EventItem model"""
    id = Column(Integer, primary_key=True)
