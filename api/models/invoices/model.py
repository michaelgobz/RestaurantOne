"""invoices model"""

from datetime import datetime

from api.core.base import declarative_base as db


class Invoice(db.Model):
    """ Invoice model"""
    __tablename__ = 'invoices'
    id = db.Column(db.String(50), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(),
                           onupdate=datetime.utcnow())

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id
        }


class InvoiceItem(db.Model):
    """InvoiceItem model"""
    __tablename__ = 'invoice_items'
    id = db.Column(db.String(50), primary_key=True)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id
        }
