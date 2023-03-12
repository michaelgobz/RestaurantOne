from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

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