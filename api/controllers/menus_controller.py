"""menus controller"""
import datetime
import uuid
from .base_controller import BaseController
from ..models import Menu , MenuItem

class MenusController:
    """The menus controller for all controllers in the api"""

    _controller:BaseController = None

    def __init__(self, controller:BaseController):
        """The constructor for the menus controller."""
        self._controller = controller

    def get_controller(self):
        """The get method for the menus controller."""
        return self._controller

    def get_menus(self):
        """Get all menus"""
        return self.get_controller().get_db_client().get_session().query(Menu).all()

    def get_menu(self, menu_id, restaurant_id):
        """Get a menu by id"""
        
        return (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(Menu)
            .filter_by(id=menu_id, restaurant_id=restaurant_id)
            .first()
        )
    def update_menu(self, menu_id, restaurant_id, data):
        """Update a menu"""
        menu = (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(Menu)
            .filter_by(id=menu_id, restaurant_id=restaurant_id)
            .first()
        )
        menu.name = data.get("name")
        menu.description = data.get("description")
        menu.price = data.get("price")
        menu.updated_at = datetime.utcnow()
        for key, value in data.items():
            setattr(menu.items, key, value)
        self.get_controller().get_db_client().get_session().commit()
        
        return menu
    def delete_menu(self, menu_id, restaurant_id):
        """Delete a menu"""
        menu = (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(Menu)
            .filter_by(id=menu_id, restaurant_id=restaurant_id)
            .first()
        )
        self.get_controller().get_db_client().get_session().delete(menu)
        self.get_controller().get_db_client().get_session().commit()
        return menu
    
    def create_menu(self, data):
        """Create a menu"""
        new_menu = Menu(
            id=str(uuid.uuid4()),
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            restaurant_id=data.get("restaurant_id"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            items=[item for item in data.get("items")]
        )
        self.get_controller().get_db_client().get_session().add(new_menu)
        self.get_controller().get_db_client().get_session().commit()
        return new_menu
     