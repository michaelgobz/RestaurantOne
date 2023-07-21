""" restaurant model """


from datetime import datetime

from api.core.base import declarative_base as db


class Restaurant(db.Model):
    """Restaurants database model"""
    __tablename__ = 'restaurants'

    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    is_operational = db.Column(db.Boolean, nullable=False)
    order_fulfilling = db.Column(db.Boolean, nullable=False)
    customers = db.Column(db.Integer, nullable=True, default=0)
    offers = db.Column(db.String(150), nullable=True)
    suppliers = db.Column(db.String(50), nullable=True)
    avatar = db.Column(db.String(3000), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    is_order_taking = db.Column(db.Boolean, nullable=False, default=True)
    subscription = db.Column(db.String(50), nullable=True)  # free, premium, gold
    

    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)

    manager_id = db.Column(db.String(50), db.ForeignKey('users.id'), nullable=False)

    menus = db.relationship("Menu",
                            backref="restaurants",
                            cascade="all, delete-orphan")
    shipments = db.relationship('Shipment', backref='restaurants')
    orders = db.relationship('Order', backref='restaurants')
    reservations = db.relationship('Reservation', backref='restaurants')
    payments = db.relationship('Payment', backref='restaurants')
    payment_methods = db.relationship('PaymentMethod', backref='restaurants')
    

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'Id': self.id,
            'Name': self.name,
            'Description': self.description,
            'Location': self.location,
            'IsOperational': self.is_operational,
            'OrderFulFilling': self.order_fulfilling,
            'Customers': self.customers,
            'Offers': self.offers,
            'Suppliers': self.suppliers,
            'Avatar': self.avatar,
            'CreatedAt': self.created_at,
            'UpdatedAt': self.updated_at,
            'Manager_id': self.manager_id,
            'Menus': [menu.serialize for menu in self.menus],
            'Shipments': [shipment.serialize for shipment in self.shipments],
            'Orders': [order.serialize for order in self.orders],
            'Reservations': [reservation.serialize for reservation in self.reservations]
        }