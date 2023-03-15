from models.db.db import DB
from ..db.models import MenuItems
from sqlalchemy.orm.exc import NoResultFound

class MenuItem:
    """Menu items class to interact with the MenuItems database
    """

    def __init__(self):
        self._db = DB()

    def register_menu_item(self, name: str, **kwargs) -> MenuItems:
        """Register a menu item in the DB"""
        try:
            menu_item = self._db.find_menu_items_by(name)
        except NoResultFound:
            menu_item = self._db.add_menu_item(name, **kwargs)

            return menu_item

        else:
            raise ValueError(f'menu item {name} already exists')