"""base model for all objects"""

from ..db import DBClient

Db = DBClient(host='restaurant-one-v1.database.windows.net', port=1433,
              user='RestaurantOne', password='JedMichael2023',
              db='restaurant')

declarative_base = Db.get_engine()


class BaseObject(declarative_base.Model):
    """Base model for all objects"""
    id = declarative_base.Column(declarative_base.Integer, primary_key=True)
