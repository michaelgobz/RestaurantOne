"""events model"""

from datetime import datetime

from api.core.base import declarative_base as db


class Event(db.Model):
    """Event model"""
    __tablename__ = 'events'
    id = db.Column(db.String(50), primary_key=True)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id
        }


class EventItem(db.Model):
    """EventItem model"""
    __tablename__ = 'event_items'
    id = db.Column(db.String(50), primary_key=True)
    event = db.Column(db.String(50), default="", nullable=True)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'event': self.event
        }