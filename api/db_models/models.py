"""data models that the api uses"""
from datetime import datetime

from api.core.base import declarative_base as db


class User(db.Model):
    """Users database model"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='customer')
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    orders = db.relationship("Order", backref="user")
    reservations = db.relationship('Reservation', backref='user')
    restaurants = db.relationship('Restaurant', backref='manager')

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
    __tablename__ = 'users_addresses'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))


class Restaurant(db.Model):
    """Restaurants database model"""
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    location = db.Column(db.String(50), nullable=True)
    is_operational = db.Column(db.Boolean, nullable=True)
    order_fulfilling = db.Column(db.Boolean, nullable=True)
    payment_methods = db.Column(db.String)
    customers = db.Column(db.Integer, nullable=False, default=0)
    offers = db.Column(db.String(50))
    suppliers = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    manager_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    menus = db.relationship("Menu",
                            backref="restaurants",
                            cascade="all, delete-orphan")
    shipments = db.relationship('Shipment', backref='restaurants')
    orders = db.relationship('Order', backref='restaurants')
    reservations = db.relationship('Reservation', backref='restaurants')


class Menu(db.Model):
    """menus database model"""
    __tablename__ = 'menus'

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
    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float, nullable=False, default=0.0)
    foods = db.Column(db.String(50), nullable=False)
    is_available = db.Column(db.Boolean, nullable=False)
    is_deliverable = db.Column(db.Boolean, nullable=False)
    duration_of_preparation = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'), nullable=False)
    carts = db.relationship('MenuItem', backref='menu_item')


class Cart(db.Model):
    """cart database model"""
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    items = db.relationship('CartItem', backref='cart', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())


class CartItem(db.Model):
    """cart items database model"""
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_items.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=1)


class Order(db.Model):
    """orders database model"""
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    items = db.relationship('OrderItem', backref='order', lazy=True)
    total_price = db.Column(db.Float, default=0.0)
    address = db.Column(db.String(255), nullable=False)
    shipment_method = db.Column(db.String(255), nullable=False)
    payment_method = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), default='pending')
    notes = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())


class OrderItem(db.Model):
    """OrderItem model"""
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_items.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)


class Reservation(db.Model):
    """Reservations database model"""
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=True)
    duration = db.Column(db.DateTime, nullable=True)
    start = db.Column(db.DateTime, nullable=True)
    end = db.Column(db.DateTime, nullable=True)
    nb_of_person = db.Column(db.Integer, nullable=False, default=0.0)
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
    __tablename__ = 'reservation_items'
    id = db.Column(db.Integer, primary_key=True)


class PaymentMethod(db.Model):
    """PaymentMethod model"""
    __tablename__ = 'payment_methods'
    id = db.Column(db.Integer, primary_key=True)


class Payment(db.Model):
    """Payment model"""
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)


class TransactionItem(db.Model):
    """TransactionItem model"""
    __tablename__ = 'transaction_items'
    id = db.Column(db.Integer, primary_key=True)


class Transaction(db.Model):
    """Transaction model"""
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=True)
    duration = db.Column(db.DateTime, nullable=True)
    start = db.Column(db.DateTime, nullable=True)
    end = db.Column(db.DateTime, nullable=True)
    nb_of_person = db.Column(db.Integer, nullable=False, default=0.0)
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
    __tablename__ = 'shipment_methods'
    id = db.Column(db.Integer, primary_key=True)


class Shipment(db.Model):
    """Shipment model"""
    __tablename__ = 'shipments'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))


class Invoice(db.Model):
    """ Invoice model"""
    __tablename__ = 'invoices'
    id = db.Column(db.Integer, primary_key=True)


class InvoiceItem(db.Model):
    """InvoiceItem model"""
    __tablename__ = 'invoice_items'
    id = db.Column(db.Integer, primary_key=True)


class Information(db.Model):
    """information model"""
    __tablename__ = 'information'
    id = db.Column(db.Integer, primary_key=True)


class Review(db.Model):
    """Review model"""
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)


class ReviewItem(db.Model):
    """ReviewItem model"""
    __tablename__ = 'review_items'
    id = db.Column(db.Integer, primary_key=True)


class Event(db.Model):
    """Event model"""
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)


class EventItem(db.Model):
    """EventItem model"""
    __tablename__ = 'event_items'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(50), default="", nullable=True)
