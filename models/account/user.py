from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
 #  Representation of a user

   __tablename__ = 'users'

   id = Column(Integer, primary_key=True)
   email = Column(String(120), unique=True, nullable=False)
   password = Column(String(60), nullable=False)
   first_name = Column(String(50), nullable=False)
   last_name = Column(String(50), nullable=False)
   phone = Column(Integer, unique=True, nullable=True)
   country = Column(String(50), nullable=True)
   location = Column(String(50), nullable=True)
   address = Column(String(150), nullable=True)
   role = Column(String(50), nullable=False)
   permissions = Column(String, nullable=False)
   avatar = Column(String(20), nullable=False, default='default.jpg')
   orders = relationship('Order', backref='user', lazy=True)
   reservations = relationship('Reservation', backref='user')
   payment_methods = Column(String, nullable=True)
   reviews = Column(String(1000), nullable=True)