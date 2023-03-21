"""data models that the api uses"""
from email.policy import default
from typing import List
from datetime import datetime
from api.core.base import declarative_base as db


class User(db.Model):
    """Users database model"""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    orders = db.relationship("Order", backref="user")
    reservations = db.relationship('Reservation', backref='user')

    # Define many-to-many relationship with Address model
    addresses = db.relationship("Address",
                                secondary="users_addresses",
                                back_populates="users")


class Address(db.Model):
    """Addresses database model"""
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    address_one = db.Column(db.String(50), nullable=False)
    address_two = db.Column(db.String(50), nullable=True)
    phone_number = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    city_area = db.Column(db.String(50), nullable=True)
    country = db.Column(db.String(50), nullable=False)
    country_area = db.Column(db.String(50), nullable=True)

    # Define many-to-many relationship with User model
    users = db.relationship("User",
                            secondary="users_addresses",
                            back_populates="addresses")


class UserAddress(db.Model):
    """Association table for many-to-many relationship"""
    __tablename__ = 'users_address'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))



class Restaurant(db.Model):
    """Restaurants database model"""
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    location = db.Column(db.String(50), nullable=True)
    is_operational = db.Column(db.Boolean, nullable=True)
    order_fulfilling = db.Column(db.Boolean, nullable=True)
    products = db.Column(db.String)
    payment_methods = db.Column(db.String)
    customers = db.Column(db.Integer, nullable=False, default=0)
    offers = db.Column(db.String(50))
    suppliers = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    menus = db.relationship("Menu",
                            backref="restaurant",
                            cascade="all, delete-orphan")
    shipments = db.relationship('Shipment', backref='restaurant')
    orders = db.relationship('Order', backref='restaurant')
    reservations = db.relationship('Reservation', backref='restaurant')


class Menu(db.Model):
    """menus database model"""
    __tablename__ = 'menu'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    restaurant_id = db.Column(db.Integer,
                              db.ForeignKey('restaurants.id'), nullable=False)
    items = db.relationship('MenuItem',
                            backref='menu', cascade="all, delete-orphan")


class MenuItem(db.Model):
    """menu items database model"""
    __tablename__ = 'menu_item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float, nullable=False, default=0)
    foods = db.Column(db.String(50), nullable=False)
    is_available = db.Column(db.Boolean, nullable=False)
    is_deliverable = db.Column(db.Boolean, nullable=False)
    duration_of_preparation = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)



class Order(db.Model):
    """orders database model"""
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    menu = db.Column(db.String(500), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(500), nullable=False)
    shipment_method = db.Column(db.String(50), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class OrderItem(db.Model):
    """OrderItem model"""
    id = db.Column(db.Integer, primary_key=True)


class Reservation(db.Model):
    """Reservations database model"""
    __tablename__ = 'reservation'

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
    menu = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    restaurant_id = db.Column(db.Integer,
                              db.ForeignKey('restaurants.id'), nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'), nullable=False)

class ReservationItem(db.Model):
    """Reservation Item model"""
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
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'),
                              nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class ShipmentMethod(db.Model):
    """Shipment method model"""
    id = db.Column(db.Integer, primary_key=True)


class Shipment(db.Model):
    """Shipment model"""
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

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

    """ReviewItem model"""
    id = db.Column(db.Integer, primary_key=True)


class Event(db.Model):
    """Event model"""
    id = db.Column(db.Integer, primary_key=True)


class EventItem(db.Model):
    """EventItem model"""
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(50), default="", nullable=True)
