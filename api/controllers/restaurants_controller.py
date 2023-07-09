""" restaurants_controller"""
import uuid
import datetime
from .base_controller import BaseController
from ..models import Restaurant


class RestaurantsController:
    """The restaurants controller for all controllers in the api"""

    _controller: BaseController = None

    def __init__(self, controller: BaseController):
        """ The constructor for the restaurants controller"""
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
    
    def update_restaurant(self, restaurant_id, data):
        """Update a restaurant"""
        restaurant = self.get_restaurant(restaurant_id)
        restaurant.name = data["name"]
        restaurant.description = data["description"]
        restaurant.location = data["location"]
        restaurant.is_operational = data["is_operational"]
        restaurant.order_fulfilling = data["order_fulfilling"]
        restaurant.avatar = data["avatar"]
        restaurant.updated_at = datetime.datetime.utcnow()
        self.get_controller().get_db_client().get_session().commit()
        return restaurant
    
    def delete_restaurant(self, restaurant_id):
        """Delete a restaurant"""
        restaurant = self.get_restaurant(restaurant_id)
        self.get_controller().get_db_client().get_session().delete(restaurant)
        self.get_controller().get_db_client().get_session().commit()
        return restaurant
    
    def get_restaurant_by_manager_id(self, manager_id):
        """Get a restaurant by manager_id"""
        return (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(Restaurant)
            .filter_by(manager_id=manager_id)
            .first()
        )
        
