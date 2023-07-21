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
    balance= db.Column(db.Float, default_value=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(),
                           onupdate=datetime.utcnow())

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'Id': self.id,
            'UserId': self.user_id,
            'RestaurantId': self.restaurant_id,
            'TotalPrice': self.total_price,
            'Address': self.address,
            'Status': self.status,
            'Notes': self.notes,
            'Balances': self.balance,
            'CreatedAt': self.created_at,
            'UpdatedAt': self.updated_at,
            'Items': [item.serialize for item in self.items],
            'Payments': [payment.serialize for payment in self.payments]
        }


class OrderItem(db.Model):
    """OrderItem model"""
    __tablename__ = 'OrderItems'

    id = db.Column(db.String(50), primary_key=True)
    order_id = db.Column(db.String(50), db.ForeignKey('orders.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    cart_id = db.Column(db.Column(db.String(50), db.ForeignKey('carts.id')))
    vat_tax = db.Column(db.Float, default_value=0.0 ,nullable=False )

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'Id': self.id,
            'OrderId': self.order_id,
            'Quantity': self.quantity,
            'Price': self.price,
            'VAT': self.vat_tax
        }