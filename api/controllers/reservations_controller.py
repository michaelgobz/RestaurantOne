""" reservations_controller"""

from .base_controller import BaseController
from ..models import Reservation


class ReservationsController:
    """The reservations controller for all controllers in the api"""

    _controller: BaseController = None

    def __init__(self, controller: BaseController):
        """ The constructor for the reservations controller"""
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
        
    def get_reservation_by_name(self, name):
        """Get a reservation by name"""
        return (
            self.get_controller().get_db_client().get_session().query(Reservation)\
                .filter_by(name=name).first()
        )
        
    def get_reservation_by_restaurant_id(self, restaurant_id):
        """Get a reservation by restaurant_id"""
        return (
            self.get_controller().get_db_client().get_session().query(Reservation)\
                .filter_by(restaurant_id=restaurant_id).first()
        )
        
    def create_reservation(self, data):
        """Create a new reservation"""
        reservation = Reservation(
            name=data["name"],
            restaurant_id=data["restaurant_id"],
            date=data["date"],
            time=data["time"],
            size=data["size"],
        )
        self.get_controller().get_db_client().get_session().add(reservation)
        self.get_controller().get_db_client().get_session().commit()
        return reservation
    
    def update_reservation(self, reservation_id, data):
        """Update a reservation"""
        reservation = self.get_reservation(reservation_id)
        reservation.name = data["name"]
        reservation.restaurant_id = data["restaurant_id"]
        reservation.date = data["date"]
        reservation.time = data["time"]
        reservation.size = data["size"]
        self.get_controller().get_db_client().get_session().commit()
        return reservation
    
    def delete_reservation(self, reservation_id):
        """Delete a reservation"""
        reservation = self.get_reservation(reservation_id)
        self.get_controller().get_db_client().get_session().delete(reservation)
        self.get_controller().get_db_client().get_session().commit()
        return reservation
    
    def get_reservation_by_date(self, date):
        """Get a reservation by date"""
        return (
            self.get_controller().get_db_client().get_session().query(Reservation)\
                .filter_by(date=date).first()
        )
    
    def get_reservation_by_time(self, time):
        """Get a reservation by time"""
        return (
            self.get_controller().get_db_client().get_session().query(Reservation)\
                .filter_by(time=time).first()
        )
        
    def cancel_reservation(self, reservation_id):
        """Cancel a reservation"""
        reservation = self.get_reservation(reservation_id)
        reservation.cancelled = True
        self.get_controller().get_db_client().get_session().commit()
        return reservation
