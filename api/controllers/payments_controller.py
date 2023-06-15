""" payments_controller"""

from .base_controller import BaseController
from ..models import Payment


class PaymentsController:
    """The payments controller for all controllers in the api"""

    _controller: BaseController = None

    def __init__(self, controller: BaseController):
        self._controller = controller

    def get_controller(self):
        """The get method for the payments controller"""
        return self._controller

    def get_payments(self):
        """Get all payments"""
        return self.get_controller().get_db_client().get_session().query(Payment).all()

    def get_payment(self, payment_id):
        """Get a payment by id"""
        return (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(Payment)
            .filter_by(id=payment_id)
            .first()
        )
