from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
 #  Representation of a user

   __tablename__ = 'users'

   id = Column(Integer, primary_key=True)
   email = Column(String(120), unique=True, nullable=False)
   password = Column(String(120), nullable=False)
   first_name = Column(String(80), nullable=False)
   last_name = Column(String(80), nullable=False)
   phone_number = Column(String(20), unique=True, nullable=False)
   country = Column(String(80), nullable=False)
   location = Column(String(80), nullable=False)
   address = Column(String(80), nullable=False)
   role = Column(String(80), nullable=False)
   permissions = Column(String, nullable=False)
   avatar = Column(String(20), nullable=False, default='default.jpg')
   orders = relationship('Order', backref='user', lazy=True)
   reservations = relationship('Reservation', backref='user')
   payment_methods = Column(String, nullable=True)
   reviews = Column(String(1000), nullable=True)

   def __repr__(self):
        return '<User %r>' % self.email
   

   

class Restaurants(Base):
# Representation of a restaurant

    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String(50), nullable=True)
    mission_statement = Column(String(50), nullable=True)
    is_operational = Column(Boolean, nullable=True)
    order_fulfilling = Column(Boolean, nullable=True)
    menus = relationship('Menu', backref='restaurant', lazy=True)
    products = Column(String)
    orders = relationship('Order', backref='restaurant', lazy=True)
    payment_methods = Column(String)
    reservations = relationship('Reservation', backref='restaurant', lazy=True)
    customers = Column(Integer, nullable=False, default=0)
    shipments = relationship('Shipment', backref='restaurant', lazy=True)
    offers = Column(String(50))
    suppliers = Column(String(50))

    def __repr__(self):
        return '<Restaurant %r>' % self.name
    


class Products(Base):
# Representation of a product

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    short_name = Column(String(50), nullable=False)
    long_name = Column(String(50), nullable=True)
    description = Column(Text, nullable=False)
    menu_category = Column(String(50), nullable=True)
    menu_item = Column(String(50), nullable=True)
    owner = Column(String(50), nullable=True)
    price = Column(Integer, nullable=False, default=0)
    varients = Column(String(50), nullable=True)
    is_available = Column(Boolean, nullable=False)
    is_deliverable = Column(Boolean, nullable=False)
    duration_of_preparation = Column(DateTime)
    max_quantity = Column(Integer, nullable=False, default=0)
    location = Column(String(50), nullable=True)

    def __repr__(self):
        return '<Product %r>' % self.short_name
    


class Menus(Base):
#    Representation of a menu

    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(50))
    items = Column(String(50))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)
    owner_restaurant_name = Column(String(50), nullable=True)

    def __repr__(self):
        return '<Menu %r>' % self.name
    


class MenuItems(Base):
#   Representation of a menu item

    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(50), nullable=True)
    price = Column(Integer, nullable=False, default=0)
    foods = Column(String(50), nullable=False)
    toppings = Column(String(50), nullable=True)
    serving_model = Column(String(50), nullable=True)
    tax_associated = Column(Integer, nullable=True)

    def __repr__(self):
        return '<Menu item %r>' % self.name
    


class Orders(Base):
#    Representation of an order

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    items = Column(String(50), nullable=False)
    total_cart_price = Column(Integer, nullable=False, default=0)
    address = Column(Text, nullable=False)
    shipment_method = Column(String(50), nullable=False)
    payment_method = Column(String(50), nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return '<Order %r>' % self.id
    


class Reservations(Base):
 #   Representation of a reservation

    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(Text, nullable=True)
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
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Reservation %r>' % self.name
    


class Shipment(Base):
# Representation of a shipment

    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(250))
    capacity = Column(Integer)
    operator = Column(String(50))
    method = Column(String(50))
    means = Column(String(50))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return '<Shipment %r>' % self.name