from models.db.db import DB
from ..db.models import Reservations

class Reservation:
    """Reservations class to interact with the Reservations database
    """

    def __init__(self):
        self._db = DB()

    def register_reservation(self, **kwargs) -> Reservations:
        """Register a reservation in the DB"""
        reservation = self._db.add_reservation(**kwargs)

        return reservation