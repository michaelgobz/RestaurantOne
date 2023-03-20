"""application entry point"""
from flask import Flask
# models
from api.db_models import Address, User, MenuItem, Menu, OrderItem, Order, \
    PaymentMethod, \
    Payment, TransactionItem, Transaction, ReservationItem, Reservation, \
    Restaurant, ShipmentMethod, Shipment, Invoice, InvoiceItem, Event, EventItem, \
    Information
from api.core.base import Db as db
from api.routes import api

# Initializing flask app
app = Flask(__name__)

# Initializing database configurations

# models

# initializing database with flask app
db.initialize_app(app)


# Route for seeing a data
app.register_blueprint(api)


# Running app
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
