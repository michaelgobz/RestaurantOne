""" shipment model """

from datetime import datetime

from api.core.base import declarative_base as db


class ShipmentMethod(db.Model):
    """Shipment method model"""
    __tablename__ = 'shipment_methods'
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    tax = db.Column(db.Float, nullable=False)
    charge = db.Column(db.Float, nullable=False)
    maximum_delivery_weight = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow,
                           )

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'tax': self.tax,
            'charge': self.charge,

        }


class Shipment(db.Model):
    """Shipment model"""
    __tablename__ = 'shipments'
    id = db.Column(db.String(50), primary_key=True)
    restaurant_id = db.Column(db.String(50), db.ForeignKey('restaurants.id'))

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id
        }
