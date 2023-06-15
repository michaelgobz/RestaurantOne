""" invoices controller """"

from .base_controller import BaseController
from ..models import  Invoice

class InvoicesController:
    _controller:BaseController = None
    
    def __init__(self, controller:BaseController):
        self._controller = controller
    
    def get_controller(self):
        return self._controller
        
    def get_invoices(self):
        return self.get_controller().get_db_client().get_session().query(Invoice).all()
        
    def get_invoice(self, invoice_id):
        return self.get_controller().get_db_client().get_session().query(Invoice)\
        .filter_by(id=invoice_id).first()
        
        