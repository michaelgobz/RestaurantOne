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
    reservation_fee = db.Column(db.Float, default_value=0.0)
    final_fee = db.Column(db.Float, default_value=0.0)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)

    # json serializer
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'Id': self.id,
            'UserId': self.user_id,
            'RestaurantId': self.restaurant_id,
            'MenuId': self.menu_id,
            'Description': self.description,
            'Duration': self.duration,
            'Start': self.start,
            'End': self.end,
            'NumberOfPersons': self.nb_of_person,
            'MenuItem': self.menu_item_id,
            'AdditionalInfo': self.additional_info,
            'Tables': self.tables,
            'Category': self.category,
            'Price': self.price,
            'ReservationFee': self.reservation_fee,
            'FinalFee': self.final_fee,
            'CreatedAt': self.created_at,
            'UpdatedAt': self.updated_at
        }
