from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

Base = declarative_base()

class Reservation(Base):
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