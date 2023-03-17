"""application entry point"""
from flask import Flask
# models
from api.db_models import Address, User, MenuItem, Menu, OrderItem, Order, \
PaymentMethod,\
Payment, TransactionItem, Transaction, ReservationItem, Reservation, \
Restaurant, ShipmentMethod, Shipment, Invoice, InvoiceItem, Event, EventItem,\
Information
from api.core.base import Db as db

from api.routes import views




# Initializing flask app
app = Flask(__name__)

# Initializing database configurations

# models
user = User()
address = Address()
menu_item =MenuItem()
menu = Menu()
order_item = OrderItem()
order = Order()
payment_method = PaymentMethod()
payment = Payment()
transaction_item = TransactionItem()
transaction = Transaction()
reservation_item = ReservationItem()
reservation = Reservation()
restaurant = Restaurant()
shipment_method = ShipmentMethod()
shipment = Shipment()
invoice = Invoice()
invoice_item = InvoiceItem()
event = Event()
event_item = EventItem()
information = Information()


#initializing database with flask app
db.initialize_app(app)

# Route registration
app.register_blueprint(views)

# Running app
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
