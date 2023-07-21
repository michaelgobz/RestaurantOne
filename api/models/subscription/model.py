from datetime import datetime

from api.core.base import declarative_base as db


class Subscription(db.Model):
    """ Subscription model"""
    __tablename__ = "subscriptions"
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow()
    )
    subscription_cost= db.Column(db.Integer(50), nullable=False)
    tenants = db.relationship('Tenant', secondary='subscriptions',
                              back_populates='subscriptions')
    
    
    @property
    def serialize(self):
        return {
            'Id':self.id,
            'Name': self.name,
            'Description':self.description,
            'CreatedAt': self.created_at,
            'UpdatedAt': self.updated_at,
            'SubscriptionCost': self.subscription_cost,
            'Tenants':[tenant.serialize for tenant in self.tenants]
        }