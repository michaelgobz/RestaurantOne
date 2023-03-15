from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from ..object.base import Base


class Order(Base):
    """Order model"""
    __tablename__ = "orders"