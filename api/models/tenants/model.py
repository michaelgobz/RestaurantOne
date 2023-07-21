""" tenants model"""

from datetime import datetime

from api.core.base import declarative_base as db


class Tenant(db.Model):
    """Tenant model"""

    __tablename__ = "tenants"
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.String(50), db.ForeignKey("users.id"))
    description = db.Column(db.String(255), nullable=False)
    subscription_id = db.Column(db.String(50), db.ForeignKey("subscriptions.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow()
    )

    # json serialization

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {"id": self.id, 
                "name": self.name, 
                "description": self.description,
                "SubscriptionId": self.subscription_id
                }
