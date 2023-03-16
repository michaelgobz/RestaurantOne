from models.db.db import DB
from ..db.models import Restaurants
from sqlalchemy.orm.exc import NoResultFound

class Restaurant:
    """Restaurant class to interact with the restaurants database
    """

    def __init__(self):
        self._db = DB()

    def register_restaurant(self, name: str, *args) -> Restaurants:
        """Register a restaurant in the DB"""
        try:
            restaurant = self._db.find_restaurant_by(name)
        except NoResultFound:
            restaurant = self._db.add_restaurant(name, *args)

            return restaurant

        else:
            raise ValueError(f'Restaurant {name} already exists')