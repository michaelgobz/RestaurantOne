"""User model"""
from typing import List
from datetime import datetime
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from .address import Address

from ..core.base import declarative_base as db


class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                          default=datetime.utcnow, editable=False)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow, editable=True)
    addresses: Mapped[List['Address']] = db.relationship("Address", backref="user",
                                                       cascade="all, delete-orphan")
