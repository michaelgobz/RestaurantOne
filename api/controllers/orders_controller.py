""" orders controller """

from .base_controller import BaseController
from ..models import Order


class OrdersController:
    """The orders controller for all controllers in the api"""

    _controller: BaseController = None

    def __init__(self, controller: BaseController):
        self._controller = controller

    def get_controller(self):
        """The get method for the orders controller"""
        return self._controller

    def get_orders(self):
        """Get all orders"""
        return self.get_controller().get_db_client().get_session().query(Order).all()

    def get_order(self, order_id):
        """Get an order by id"""
        return (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(Order)
            .filter_by(id=order_id)
            .first()
        )
