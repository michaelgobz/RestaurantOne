"""menus controller"""

from .base_controller import BaseController
from ..models import Menu

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

    def get_menu(self, menu_id):
        """Get a menu by id"""
        return (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(Menu)
            .filter_by(id=menu_id)
            .first()
        )
        