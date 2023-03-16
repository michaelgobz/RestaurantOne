from models.db.db import DB
from ..db.models import Menus
from sqlalchemy.orm.exc import NoResultFound

class Menu:
    """menu class to interact with the menus database
    """

    def __init__(self):
        self._db = DB()

    def register_menu(self, name: str, *args) -> Menus:
        """Register a menu in the DB"""
        try:
            menu = self._db.find_menu_by(name)
        except NoResultFound:
            menu = self._db.add_menu(name, *args)

            return menu

        else:
            raise ValueError(f'menu {name} already exists')