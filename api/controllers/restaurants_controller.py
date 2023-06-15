""" restaurants_controller"""

from .base_controller import BaseController
from ..models import Restaurant


class RestaurantsController:
    """The restaurants controller for all controllers in the api"""

    _controller: BaseController = None

    def __init__(self, controller: BaseController):
        self._controller = controller

    def get_controller(self):
        """The get method for the restaurants controller"""
        return self._controller

    def get_restaurants(self):
        """Get all restaurants"""
        return (
            self.get_controller().get_db_client().get_session().query(Restaurant).all()
        )

    def get_restaurant(self, restaurant_id):
        """Get a restaurant by id"""
        return (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(Restaurant)
            .filter_by(id=restaurant_id)
            .first()
        )
