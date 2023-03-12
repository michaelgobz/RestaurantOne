from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship

Base = declarative_base()

class Restaurant(Base):
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