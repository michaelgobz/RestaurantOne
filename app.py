"""application entry point"""
from flask import Flask
# models
from api.db_models import Address, User, MenuItem, Menu, OrderItem, Order, \
    PaymentMethod, \
    Payment, TransactionItem, Transaction, ReservationItem, Reservation, \
    Restaurant, ShipmentMethod, Shipment, Invoice, InvoiceItem, Event, EventItem, \
    Information
from api.core.base import Db as db

# Initializing flask app
app = Flask(__name__)

# Initializing database configurations

# models

# initializing database with flask app
db.initialize_app(app)


# Route for seeing a data
@app.route('/')
def initial():
    """initial route
    welcome route

    Returns:
        _object_: welcome parameters
    """

    return {
        "message": "welcome to the Our Platform",
        "company": "RestaurantOne",
        "location": "Kampala",
        "year": 2023,
        "month": "March",
        "Country": "Uganda",
        "Project": "Alx-webstack project",
        "supervisor": "Alx-SE Mentors",
    }


# Running app
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
