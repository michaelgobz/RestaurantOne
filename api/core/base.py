"""base model for all objects"""

from ..db import DBClient

Db = DBClient(host='localhost', port=5433,
              user='RestaurantOne', password='JedMichael2023',
              db='restaurant')

declarative_base = Db.get_engine()

