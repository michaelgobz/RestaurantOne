"""base model for all objects"""

from app import Db 

declarative_base = Db.get_engine()

class BaseObject(declarative_base.Model):
    """Base model for all objects"""
    pass