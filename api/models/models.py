"""data models that the api uses"""
from datetime import datetime

from api.core.base import declarative_base as db


class User(db.Model):
    """Users database model"""
    __tablename__ = 'users'

    id = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    salt = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=True, default='customer')
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    phone_number = db.Column(db.String(50), nullable=False)
    is_verified = db.Column(db.Boolean, nullable=False, default=False)
    password_reset_token = db.Column(db.String(255), nullable=True)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)

    payment_methods = db.relationship('PaymentMethod', backref='user', lazy=True)
    restaurants = db.relationship('Restaurant', backref='manager')
    orders = db.relationship("Order", backref="users")
    reservations = db.relationship('Reservation', backref='users')

    # Define many-to-many relationship with Address model
    addresses = db.relationship("Address",
                                secondary="users_addresses",
                                back_populates="users")

    # json serialization

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role,
            'created_at': self.created_at,
            'phone_number': self.phone_number,
            'is_verified': self.is_verified,
            'password_reset_token': self.password_reset_token,
            'updated_at': self.updated_at,
            'payment_methods': [payment_method.serialize
                                for payment_method in self.payment_methods],
            'orders': [order.serialize for order in self.orders],
            'reservations': [reservation.serialize for reservation in self.reservations],
            'restaurants': [restaurant.serialize for restaurant in self.restaurants],
            'addresses': [address.serialize for address in self.addresses],
        }


class Address(db.Model):
    """Addresses database model"""
    __tablename__ = 'addresses'

    id = db.Column(db.String(50), primary_key=True)
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

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'address_one': self.address_one,
            'address_two': self.address_two,
            'phone_number': self.phone_number,
            'city': self.city,
            'city_area': self.city_area,
            'country': self.country,
            'country_area': self.country_area,
            'users': [user.serialize for user in self.users]
        }


class UserAddress(db.Model):
    """Association table for many-to-many relationship"""
    __tablename__ = 'users_addresses'

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id'))
    address_id = db.Column(db.String(50), db.ForeignKey('addresses.id'))

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'address_id': self.address_id
        }


class Restaurant(db.Model):
    """Restaurants database model"""
    __tablename__ = 'restaurants'

    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    is_operational = db.Column(db.Boolean, nullable=False)
    order_fulfilling = db.Column(db.Boolean, nullable=False)
    customers = db.Column(db.Integer, nullable=True, default=0)
    offers = db.Column(db.String(150), nullable=True)
    suppliers = db.Column(db.String(50), nullable=True)
    avatar = db.Column(db.String(3000), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)

    manager_id = db.Column(db.String(50), db.ForeignKey('users.id'), nullable=False)

    menus = db.relationship("Menu",
                            backref="restaurants",
                            cascade="all, delete-orphan")
    shipments = db.relationship('Shipment', backref='restaurants')
    orders = db.relationship('Order', backref='restaurants')
    reservations = db.relationship('Reservation', backref='restaurants')

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'is_operational': self.is_operational,
            'order_fulfilling': self.order_fulfilling,
            'customers': self.customers,
            'offers': self.offers,
            'suppliers': self.suppliers,
            'avatar': self.avatar,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'manager_id': self.manager_id,
            'menus': [menu.serialize for menu in self.menus],
            'shipments': [shipment.serialize for shipment in self.shipments],
            'orders': [order.serialize for order in self.orders],
            'reservations': [reservation.serialize for reservation in self.reservations]
        }


class Menu(db.Model):
    """menus database model"""
    __tablename__ = 'menus'

    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    category = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    restaurant_id = db.Column(db.String(50),
                              db.ForeignKey('restaurants.id'), nullable=False)
    items = db.relationship('MenuItem',
                            backref='menu', cascade="all, delete-orphan")
    carts = db.relationship('CartItem', backref='menu_item')
    reservations = db.relationship('Reservation', backref='menu_item')

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'restaurant_id': self.restaurant_id,
            'items': [item.serialize for item in self.items],
            'carts': [cart.serialize for cart in self.carts],
            'reservations': [reservation.serialize for reservation in self.reservations]
        }


class MenuItem(db.Model):
    """menu items database model"""
    __tablename__ = 'menu_items'

    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    foods = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0.0)
    is_available = db.Column(db.Boolean, nullable=False)
    is_deliverable = db.Column(db.Boolean, nullable=False)
    rating = db.Column(db.Integer(), nullable=False, default=0)
    duration_of_preparation = db.Column(db.Integer(), nullable=False)
    avatar = db.Column(db.String(3000), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    menu_id = db.Column(db.String(50), db.ForeignKey('menus.id'), nullable=False)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'foods': self.foods,
            'category': self.category,
            'price': self.price,
            'isAvailable': self.is_available,
            'isDeliverable': self.is_deliverable,
            'rating': self.rating,
            'duration': self.duration_of_preparation,
            'avatar': self.avatar,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'menu_id': self.menu_id
        }


class Cart(db.Model):
    """cart database model"""
    __tablename__ = 'carts'

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id'), nullable=False)
    items = db.relationship('CartItem', backref='cart', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(),
                           onupdate=datetime.utcnow())

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'items': [item.serialize for item in self.items]
        }


class CartItem(db.Model):
    """cart items database model"""
    __tablename__ = 'cart_items'

    id = db.Column(db.String(50), primary_key=True)
    cart_id = db.Column(db.String(50), db.ForeignKey('carts.id'), nullable=False)
    menu_id = db.Column(db.String(50), db.ForeignKey('menus.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'cart_id': self.cart_id,
            'menu_id': self.menu_id,
            'price': self.price,
            'quantity': self.quantity
        }


class Order(db.Model):
    """orders database model"""
    __tablename__ = 'orders'

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id'), nullable=False)
    restaurant_id = db.Column(db.String(50), db.ForeignKey('restaurants.id'),
                              nullable=False)
    items = db.relationship('OrderItem', backref='order', lazy=True)
    total_price = db.Column(db.Float, default=0.0)
    address = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), default='pending')
    notes = db.Column(db.String(255), nullable=True)
    payments = db.relationship('Payment', backref='order', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(),
                           onupdate=datetime.utcnow())

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'restaurant_id': self.restaurant_id,
            'total_price': self.total_price,
            'address': self.address,
            'status': self.status,
            'notes': self.notes,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'items': [item.serialize for item in self.items],
            'payments': [payment.serialize for payment in self.payments]
        }


class OrderItem(db.Model):
    """OrderItem model"""
    __tablename__ = 'order_items'

    id = db.Column(db.String(50), primary_key=True)
    order_id = db.Column(db.String(50), db.ForeignKey('orders.id'), nullable=False)
    menu_id = db.Column(db.String(50), db.ForeignKey('menus.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'order_id': self.order_id,
            'menu_id': self.menu_id,
            'quantity': self.quantity,
            'price': self.price

        }


class Reservation(db.Model):
    """Reservations database model"""
    __tablename__ = 'reservations'

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50),
                        db.ForeignKey('users.id'), nullable=False)
    restaurant_id = db.Column(db.String(50),
                              db.ForeignKey('restaurants.id'), nullable=False)
    menu_id = db.Column(db.String(50), db.ForeignKey('menus.id'), nullable=True)
    description = db.Column(db.String(200), nullable=True)
    duration = db.Column(db.DateTime, nullable=True)
    start = db.Column(db.DateTime, nullable=True)
    end = db.Column(db.DateTime, nullable=True)
    nb_of_person = db.Column(db.Integer, nullable=False, default=0)
    menu_item_id = db.Column(db.String(50), db.ForeignKey(
        'menu_items.id'), nullable=False)
    additional_info = db.Column(db.String(200), nullable=True)
    tables = db.Column(db.Integer, nullable=True)
    category = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float, nullable=True, default=0.0)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'restaurant_id': self.restaurant_id,
            'menu_id': self.menu_id,
            'description': self.description,
            'duration': self.duration,
            'start': self.start,
            'end': self.end,
            'nb_of_person': self.nb_of_person,
            'menu_item_id': self.menu_item_id,
            'additional_info': self.additional_info,
            'tables': self.tables,
            'category': self.category,
            'price': self.price,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class PaymentMethod(db.Model):
    """PaymentMethod model"""
    __tablename__ = 'payment_methods'

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id'),
                        nullable=False)
    type = db.Column(db.String(50), nullable=False)
    last4 = db.Column(db.String(4), nullable=True)
    exp_month = db.Column(db.Integer, nullable=True)
    exp_year = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    payments = db.relationship('Payment', backref='payment_method', lazy=True)

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'type': self.type,
            'last4': self.last4,
            'exp_month': self.exp_month,
            'exp_year': self.exp_year,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'payments': [payment.serialize for payment in self.payments]
        }


class Payment(db.Model):
    """Payment model"""
    __tablename__ = 'payments'

    id = db.Column(db.String(50), primary_key=True)
    order_id = db.Column(db.String(50), db.ForeignKey(
        'orders.id'), nullable=True)
    payment_method_id = db.Column(db.String(50), db.ForeignKey('payment_methods.id'),
                                  nullable=False)
    amount = db.Column(db.Float, default=0.0)
    currency = db.Column(db.String(10), default='USD')
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    transactions = db.relationship('Transaction', backref='payment', lazy=True)
    reservation_id = db.Column(db.String(50), db.ForeignKey(
        'reservations.id'), nullable=True)

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'order_id': self.order_id,
            'payment_method_id': self.payment_method_id,
            'amount': self.amount,
            'currency': self.currency,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'reservation_id': self.reservation_id,
            'transactions': [t.serialize for t in self.transactions]
        }


class Transaction(db.Model):
    """Transaction model"""
    __tablename__ = 'transactions'

    id = db.Column(db.String(50), primary_key=True)
    payment_id = db.Column(db.String(50), db.ForeignKey('payments.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'payment_id': self.payment_id,
            'amount': self.amount,
            'currency': self.currency,
            'type': self.type,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class ShipmentMethod(db.Model):
    """Shipment method model"""
    __tablename__ = 'shipment_methods'
    id = db.Column(db.String(50), primary_key=True)

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id
        }


class Shipment(db.Model):
    """Shipment model"""
    __tablename__ = 'shipments'
    id = db.Column(db.String(50), primary_key=True)
    restaurant_id = db.Column(db.String(50), db.ForeignKey('restaurants.id'))

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id
        }


class Invoice(db.Model):
    """ Invoice model"""
    __tablename__ = 'invoices'
    id = db.Column(db.String(50), primary_key=True)

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id
        }


class InvoiceItem(db.Model):
    """InvoiceItem model"""
    __tablename__ = 'invoice_items'
    id = db.Column(db.String(50), primary_key=True)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id
        }


class Information(db.Model):
    """information model"""
    __tablename__ = 'information'
    id = db.Column(db.String(50), primary_key=True)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id
        }


class Review(db.Model):
    """Review model"""
    __tablename__ = 'reviews'
    id = db.Column(db.String(50), primary_key=True)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id
        }


class ReviewItem(db.Model):
    """ReviewItem model"""
    __tablename__ = 'review_items'
    id = db.Column(db.String(50), primary_key=True)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id
        }


class Event(db.Model):
    """Event model"""
    __tablename__ = 'events'
    id = db.Column(db.String(50), primary_key=True)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id
        }


class EventItem(db.Model):
    """EventItem model"""
    __tablename__ = 'event_items'
    id = db.Column(db.String(50), primary_key=True)
    event = db.Column(db.String(50), default="", nullable=True)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'event': self.event
        }


class VerificationToken(db.Model):
    """VerificationToken model"""
    __tablename__ = 'verification_tokens'
    id = db.Column(db.String(50), primary_key=True)
    token = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    user_id = db.Column(db.String(50), db.ForeignKey(
        'users.id'), nullable=False)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format
        """
        return {
            'id': self.id,
            'token': self.token,
            'created_at': self.created_at,
            'user_id': self.user_id

        }
