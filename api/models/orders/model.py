"""orders model"""

from datetime import datetime

from api.core.base import declarative_base as db


class Order(db.Model):
    """orders database model"""
    __tablename__ = 'orders'

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id'), nullable=False)
    restaurant_id = db.Column(db.String(50), db.ForeignKey('restaurants.id'),
                              nullable=False)
    items = db.relationship('OrderItem', backref='order', lazy=True)
    total_price = db.Column(db.Float, default=0.0)
    address = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), default='pending')
    notes = db.Column(db.String(255), nullable=True)
    payments = db.relationship('Payment', backref='order', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(),
                           onupdate=datetime.utcnow())

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'restaurant_id': self.restaurant_id,
            'total_price': self.total_price,
            'address': self.address,
            'status': self.status,
            'notes': self.notes,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'items': [item.serialize for item in self.items],
            'payments': [payment.serialize for payment in self.payments]
        }


class OrderItem(db.Model):
    """OrderItem model"""
    __tablename__ = 'order_items'

    id = db.Column(db.String(50), primary_key=True)
    order_id = db.Column(db.String(50), db.ForeignKey('orders.id'), nullable=False)
    menu_id = db.Column(db.String(50), db.ForeignKey('menus.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'order_id': self.order_id,
            'menu_id': self.menu_id,
            'quantity': self.quantity,
            'price': self.price

        }