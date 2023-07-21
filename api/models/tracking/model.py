"""tokens model"""

from datetime import datetime

from api.core.base import declarative_base as db


class TrackingToken(db.Model):
    """Tracking token model"""
    __tablename__ = 'TrackingTokens'
    id = db.Column(db.String(50), primary_key=True)
    token = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    restaurant_id = db.Column(db.String(50), db.ForeignKey(
        'restaurants.id'), nullable=False)
    order_id =  db.Column(db.String(50), db.ForeignKey(
        'orders.id'), nullable=False)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format
        """
        return {
            'Id': self.id,
            'Token': self.token,
            'CreatedAt': self.created_at,
            'Restaurant': self.restaurant_id,
            'order_id': self.order_id
        }