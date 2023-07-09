"""events model"""

from datetime import datetime

from api.core.base import declarative_base as db


class Information(db.Model):
    """information model"""
    __tablename__ = 'information'
    id = db.Column(db.String(50), primary_key=True)
    short_description = db.Column(db.String(50), nullable=False)
    detailed_description = db.Column(db.String(1024), nullable=False)
    

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id
        }


class Event(db.Model):
    """Event model"""
    __tablename__ = 'events'
    id = db.Column(db.String(50), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(),
                           onupdate=datetime.utcnow())
    event_items = db.relationship("EventItem", backref="events")

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
    owner = db.Column(db.String(50), default="", nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())
    info = db.relationship("Information", backref="event_items")
    
    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'event': self.event
        }
