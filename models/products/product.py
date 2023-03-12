from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime

Base = declarative_base()

class Product(Base):
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