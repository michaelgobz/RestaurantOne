""" reviews model """

from datetime import datetime

from api.core.base import declarative_base as db


class ReservationReview(db.Model):
    """Review model"""
    __tablename__ = 'reservation_reviews'
    id = db.Column(db.String(50), primary_key=True)
    reservation_id = db.Column(db.String(50), db.ForeignKey('reservations.id'))
    restaurant_id = db.Column(db.String(50), db.ForeignKey('restaurants.id'))
    review_item_id = db.Column(db.String(50), db.ForeignKey('review_items.id'))

    # json serialization

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'reservation_id': self.reservation_id,
            'restaurant_id': self.restaurant_id,

        }


class MenuItemReview(db.Model):
    """Review model"""
    __tablename__ = 'menuitem_reviews'
    id = db.Column(db.String(50), primary_key=True)
    menu_item_id = db.Column(db.String(50), db.ForeignKey('menu_items.id'))
    review_item_id = db.Column(db.String(50), db.ForeignKey('review_items.id'))

    # json serialization

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'menu_item_id': self.menu_item_id,
            'review_item_id': self.review_item_id
        }


class ReviewItem(db.Model):
    """ReviewItem model"""
    __tablename__ = 'review_items'
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)
    description = db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(),
                           onupdate=datetime.utcnow())

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'rating': self.rating,
            'description': self.description,
            'message': self.message,
            'created_at': self.created_at
        }
