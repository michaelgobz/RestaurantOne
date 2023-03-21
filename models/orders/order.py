from models.db.db import DB
from ..db.models import Orders

class Order:
    """Menu items class to interact with the menus database
    """

    def __init__(self):
        self._db = DB()

    def register_order(self, items: list, *args) -> Orders:
        """Register a menu item in the DB"""
        order = self._db.add_order(items, *args)

        return order