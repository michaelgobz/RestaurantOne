""" menu_items_controller"""

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
