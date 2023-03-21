from models.db.db import DB
from ..db.models import Products
from sqlalchemy.orm.exc import NoResultFound

class Product:
    """Product class to interact with the Products database
    """

    def __init__(self):
        self._db = DB()

    def register_product(self, short_name: str, *args) -> Products:
        """Register a product in the DB"""
        try:
            product = self._db.find_product_by(short_name)
        except NoResultFound:
            product = self._db.add_product(short_name, *args)

            return product

        else:
            raise ValueError(f'Product {short_name} already exists')