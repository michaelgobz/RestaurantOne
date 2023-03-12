from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Menu(Base):
#    Representation of a menu

    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(50))
    items = Column(String(50))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)
    owner_restaurant_name = Column(String(50), nullable=True)