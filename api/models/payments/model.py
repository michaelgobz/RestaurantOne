""" payments model"""

from datetime import datetime

from api.core.base import declarative_base as db


class PaymentMethod(db.Model):
    """PaymentMethod model"""
    __tablename__ = 'payment_methods'

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id'),
                        nullable=False)
    type = db.Column(db.String(50), nullable=False)
    last4 = db.Column(db.String(4), nullable=True)
    exp_month = db.Column(db.Integer, nullable=True)
    exp_year = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    payments = db.relationship('Payment', backref='payment_method', lazy=True)
    restaurants = db.relationship('Restaurant', backref='payment_method', lazy=True)
    

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'type': self.type,
            'last4': self.last4,
            'exp_month': self.exp_month,
            'exp_year': self.exp_year,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'payments': [payment.serialize for payment in self.payments]
        }


class Payment(db.Model):
    """Payment model"""
    __tablename__ = 'payments'

    id = db.Column(db.String(50), primary_key=True)
    order_id = db.Column(db.String(50), db.ForeignKey(
        'orders.id'), nullable=True)
    payment_method_id = db.Column(db.String(50), db.ForeignKey('payment_methods.id'),
                                  nullable=False)
    amount = db.Column(db.Float, default=0.0)
    currency = db.Column(db.String(10), default='USD')
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    transactions = db.relationship('Transaction', backref='payment', lazy=True)
    reservation_id = db.Column(db.String(50), db.ForeignKey(
        'reservations.id'), nullable=True)

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'order_id': self.order_id,
            'payment_method_id': self.payment_method_id,
            'amount': self.amount,
            'currency': self.currency,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'reservation_id': self.reservation_id,
            'transactions': [t.serialize for t in self.transactions]
        }


class Transaction(db.Model):
    """Transaction model"""
    __tablename__ = 'transactions'

    id = db.Column(db.String(50), primary_key=True)
    payment_id = db.Column(db.String(50), db.ForeignKey('payments.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'payment_id': self.payment_id,
            'amount': self.amount,
            'currency': self.currency,
            'type': self.type,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
