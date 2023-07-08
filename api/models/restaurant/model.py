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
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'is_operational': self.is_operational,
            'order_fulfilling': self.order_fulfilling,
            'customers': self.customers,
            'offers': self.offers,
            'suppliers': self.suppliers,
            'avatar': self.avatar,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'manager_id': self.manager_id,
            'menus': [menu.serialize for menu in self.menus],
            'shipments': [shipment.serialize for shipment in self.shipments],
            'orders': [order.serialize for order in self.orders],
            'reservations': [reservation.serialize for reservation in self.reservations]
        }