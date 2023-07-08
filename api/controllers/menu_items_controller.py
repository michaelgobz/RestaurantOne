""" menu_items_controller"""
import datetime
import uuid
from .base_controller import BaseController
from ..models import MenuItem


class MenuItemsController:
    """The menu items controller for all controllers in the api"""

    _controller: BaseController = None

    def __init__(self, controller: BaseController):
        self._controller = controller

    def get_controller(self):
        """The get method for the menu items controller"""
        return self._controller

    def get_menu_items(self):
        """Get all menu items"""
        return self.get_controller().get_db_client().get_session().query(MenuItem).all()

    def get_menu_item(self, menu_item_id):
        """Get a menu item by id"""
        return (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(MenuItem)
            .filter_by(id=menu_item_id)
            .first()
        )
        
    def add_reservation_associated_with_menu_item \
        (self, menu_item_id, restaurant_id, data):
        """Add a reservation"""
        menu = (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(MenuItem)
            .filter_by(id=menu_item_id, restaurant_id=restaurant_id)
            .first()
        )
        menu.reservations.append(data)
        self.get_controller().get_db_client().get_session().commit()
        return menu
    
    def capture_cart_associated_with_menu(self, menu_item_id, restaurant_id, cart):
        """Capture a cart associated with a menu"""
        menu = (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(MenuItem)
            .filter_by(id=menu_item_id, restaurant_id=restaurant_id)
            .first()
        )
        menu.cart.append(cart)
        self.get_controller().get_db_client().get_session().commit()
        return menu
    
    
    def get_menu_items_by_menu_id(self, menu_id, restaurant_id):
        """Get all menu items by menu id"""
        return (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(MenuItem)
            .filter_by(menu_id=menu_id, restaurant_id=restaurant_id)
            .all()
        )
        
    def update_menu_item(self, menu_item_id, restaurant_id, data):
        """Update a menu item"""
        menu_item = (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(MenuItem)
            .filter_by(id=menu_item_id, restaurant_id=restaurant_id)
            .first()
        )
        menu_item.name = data.get("name")
        menu_item.description = data.get("description")
        menu_item.price = data.get("price")
        menu_item.updated_at = datetime.utcnow()
        menu_item.foods = data.get("foods")
        self.get_controller().get_db_client().get_session().commit()
        return menu_item
    
    def delete_menu_item(self, menu_item_id, restaurant_id):
        """Delete a menu item"""
        menu_item = (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(MenuItem)
            .filter_by(id=menu_item_id, restaurant_id=restaurant_id)
            .first()
        )
        self.get_controller().get_db_client().get_session().delete(menu_item)
        self.get_controller().get_db_client().get_session().commit()
        return menu_item
    
    def create_menu_item(self, menu_id, restaurant_id, data):
        """Create a menu item"""
        menu_item = MenuItem(
            id=str(uuid.uuid4()),
            name=data.get("name"),
            description=data.get("description"),
            category=data.get("category"),
            price=data.get("price"),
            restaurant_id=restaurant_id,
            menu_id=menu_id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            foods=data.get("foods"),
            isAvailable=data.get("isAvailable"),
            isDeliverable=data.get("isDeliverable"),
            duration_to_prepare=data.get("duration_to_prepare"),
            avatar=data.get("avatar"),
            
        )
        self.get_controller().get_db_client().get_session().add(menu_item)
        self.get_controller().get_db_client().get_session().commit()
        return menu_item
    
    def publish_menu_item(self, menu_item_id, restaurant_id):
        """Publish a menu item"""
        menu_item = (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(MenuItem)
            .filter_by(id=menu_item_id, restaurant_id=restaurant_id)
            .first()
        )
        menu_item.isAvailable = True
        self.get_controller().get_db_client().get_session().commit()
        return menu_item
    
    def make_menu_item_deliverable(self, menu_item_id, restaurant_id):
        """Make a menu item deliverable"""
        menu_item = (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(MenuItem)
            .filter_by(id=menu_item_id, restaurant_id=restaurant_id)
            .first()
        )
        menu_item.isDeliverable = True
        self.get_controller().get_db_client().get_session().commit()
        return menu_item
