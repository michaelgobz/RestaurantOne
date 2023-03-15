"""base model for all objects"""

from ..db import DBClient

Db = DBClient(host='localhost', port=5432,
              user='postgres', password='postgres',
              db='postgres')

declarative_base = Db.get_engine()


class BaseObject(declarative_base.Model):
    """Base model for all objects"""
    id = declarative_base.Column(declarative_base.Integer, primary_key=True)