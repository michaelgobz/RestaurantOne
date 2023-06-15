""" tracking controller """"

from .base_controller import BaseController
from ..models import Tracking

class TrackingController:
    """The tracking controller for all controllers in the api"""
    _controller:BaseController = None
    
    def __init__(self, controller:BaseController):
        self._controller = controller
    
    def get_controller(self):
        """The get method for the tracking controller"""
        return self._controller
        
    def get_trackings(self):
        """Get all trackings"""
        return self.get_controller().get_db_client().get_session().query(Tracking).all()
        
    def get_tracking(self, tracking_id):
        """ Get a tracking by id"""
        return self.get_controller().get_db_client().get_session().query(Tracking)\
        .filter_by(id=tracking_id).first()
        
        