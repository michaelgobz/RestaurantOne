from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey

Base = declarative_base()

class Order(Base):
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