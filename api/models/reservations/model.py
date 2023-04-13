"""reservation model"""


from datetime import datetime

from api.core.base import declarative_base as db


class Reservation(db.Model):
    """Reservations database model"""
    __tablename__ = 'reservations'

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50),
                        db.ForeignKey('users.id'), nullable=False)
    restaurant_id = db.Column(db.String(50),
                              db.ForeignKey('restaurants.id'), nullable=False)
    menu_id = db.Column(db.String(50), db.ForeignKey(
        'menus.id'), nullable=True)
    description = db.Column(db.String(200), nullable=True)
    duration = db.Column(db.DateTime, nullable=True)
    start = db.Column(db.DateTime, nullable=True)
    end = db.Column(db.DateTime, nullable=True)
    nb_of_person = db.Column(db.Integer, nullable=False, default=0)
    menu_item_id = db.Column(db.String(50), db.ForeignKey(
        'menu_items.id'), nullable=False)
    additional_info = db.Column(db.String(200), nullable=True)
    tables = db.Column(db.Integer, nullable=True)
    category = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float, nullable=True, default=0.0)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'restaurant_id': self.restaurant_id,
            'menu_id': self.menu_id,
            'description': self.description,
            'duration': self.duration,
            'start': self.start,
            'end': self.end,
            'nb_of_person': self.nb_of_person,
            'menu_item_id': self.menu_item_id,
            'additional_info': self.additional_info,
            'tables': self.tables,
            'category': self.category,
            'price': self.price,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
