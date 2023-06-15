""" reservations_controller"""

from .base_controller import BaseController
from ..models import Reservation


class ReservationsController:
    """The reservations controller for all controllers in the api"""

    _controller: BaseController = None

    def __init__(self, controller: BaseController):
        self._controller = controller

    def get_controller(self):
        """The get method for the reservations controller"""
        return self._controller

    def get_reservations(self):
        """Get all reservations"""
        return (
            self.get_controller().get_db_client().get_session().query(Reservation).all()
        )

    def get_reservation(self, reservation_id):
        """Get a reservation by id"""
        return (
            self.get_controller()
            .get_db_client()
            .get_session()
            .query(Reservation)
            .filter_by(id=reservation_id)
            .first()
        )
