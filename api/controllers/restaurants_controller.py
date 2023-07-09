""" restaurants_controller"""
import uuid
import datetime
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
    
    def get_restaurant_by_name(self, name):
        """Get a restaurant by name"""
        return (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(Restaurant)
            .filter_by(name=name)
            .first()
        )
        
    def get_restaurant_by_location(self, location):
        """Get a restaurant by location"""
        return (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(Restaurant)
            .filter_by(location=location)
            .first()
        )
        
    def create_restaurant(self, data):
        """Create a restaurant"""
        restaurant = Restaurant(
            id = uuid.uuid4(),
            name = data["name"],
            description = data["description"],
            location = data["location"],
            is_operational = data["is_operational"],
            order_fulfilling = data["order_fulfilling"],
            avatar = data["avatar"],
            created_at = datetime.datetime.utcnow(),
            updated_at = datetime.datetime.utcnow(),
            manager_id = data["manager_id"],
            
        )
        self.get_controller().get_db_client().get_session().add(restaurant)
        self.get_controller().get_db_client().get_session().commit()
        return restaurant
