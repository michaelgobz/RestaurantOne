""" invoices controller """"

from .base_controller import BaseController
from ..models import  Invoice, User

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
        
    def generate_invoice(self, data):
        invoice = Invoice(
            name=data["name"],
            restaurant_id=data["restaurant_id"],
            date=data["date"],
            time=data["time"],
            size=data["size"],
            price=data["price"],
            paid=data["paid"],
            )
        self.get_controller().get_db_client().get_session().add(invoice)
        self.get_controller().get_db_client().get_session().commit()
        return invoice
        
    def send_invoice_to_customer(self, invoice_id, user_id):
        invoice = self.get_invoice(invoice_id)
        user = self.get_controller().get_db_client().get_session().query(User)\
            .filter_by(id=user_id).first()
        invoice.paid = True
        self.get_controller().get_db_client().get_session().commit()
        return invoice
        
        