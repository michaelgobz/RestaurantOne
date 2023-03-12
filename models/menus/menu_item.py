from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

Base = declarative_base()

class MenuItem(Base):
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