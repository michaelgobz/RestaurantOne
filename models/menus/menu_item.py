"""menu item model"""
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from ..core.base import declarative_base as db


class MenuItem(db.Model):
    """menu item model"""
    id = db.Column(Integer, primary_key=True)