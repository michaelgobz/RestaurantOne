""" reviews model """

from datetime import datetime

from api.core.base import declarative_base as db


class ReservationReview(db.Model):
    """Review model"""
    __tablename__ = 'ReservationReviews'
    id = db.Column(db.String(50), primary_key=True)
    reservation_id = db.Column(db.String(50), db.ForeignKey('reservations.id'))
    restaurant_id = db.Column(db.String(50), db.ForeignKey('restaurants.id'))
    reviews = db.relationship('ReviewItem', secondary='ReviewItems', back_populate='ReviewItems')

    # json serialization

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'Id': self.id,
            'ReservationId': self.reservation_id,
            'RestaurantId': self.restaurant_id,
            'Reviews': [review.serialize for review in self.reviews]
        }


class MenuItemReview(db.Model):
    """Review model"""
    __tablename__ = 'MenuItemReviews'
    id = db.Column(db.String(50), primary_key=True)
    menu_item_id = db.Column(db.String(50), db.ForeignKey('menu_items.id'))
    reviews = db.relationship('ReviewItem', secondary='ReviewItems', back_populate='ReviewItems')

    # json serialization

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'MenuItem': self.menu_item_id,
            'Reviews': [review.serialize for review in self.reviews]
        }


class ReviewItem(db.Model):
    """ReviewItem model"""
    __tablename__ = 'ReviewItems'
    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id'))
    name = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(),
                           onupdate=datetime.utcnow())

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'Id': self.id,
            'User': self.user_id,
            'Name': self.name,
            'Rating': self.rating,
            'Description': self.description,
            'UpdatedAt': self.updated_at
        }
