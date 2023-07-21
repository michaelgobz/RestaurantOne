""" menus model"""

from datetime import datetime

from api.core.base import declarative_base as db


class Menu(db.Model):
    """menus database model"""
    __tablename__ = 'menus'

    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    category = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow),
    isAvailable = db.Column(db.Boolean, nullable=False, default=True)
    restaurant_id = db.Column(db.String(50),
                              db.ForeignKey('restaurants.id'), nullable=False)
    items = db.relationship('MenuItem',
                            backref='menu', cascade="all, delete-orphan")

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'Id': self.id,
            'Name': self.name,
            'Description': self.description,
            'Category': self.category,
            'CreatedAt': self.created_at,
            'UpdatedAt': self.updated_at,
            'RestaurantId': self.restaurant_id,
            'Items': [item.serialize for item in self.items],
        }


class MenuItem(db.Model):
    """menu items database model"""
    __tablename__ = 'menu_items'

    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    foods = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0.0)
    is_available = db.Column(db.Boolean, nullable=False)
    is_deliverable = db.Column(db.Boolean, nullable=False)
    rating = db.Column(db.Integer(), nullable=False, default=0)
    duration_of_preparation = db.Column(db.Integer(), nullable=False)
    avatar = db.Column(db.String(3000), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    carts = db.relationship('CartItem', backref='menu_item')
    reservations = db.relationship('Reservation', backref='menu_item')
    menu_id = db.Column(db.String(50), db.ForeignKey('menus.id'), nullable=False)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'Id': self.id,
            'Name': self.name,
            'Description': self.description,
            'Foods': self.foods,
            'Category': self.category,
            'Price': self.price,
            'IsAvailable': self.is_available,
            'IsDeliverable': self.is_deliverable,
            'Rating': self.rating,
            'Duration': self.duration_of_preparation,
            'Avatar': self.avatar,
            'CreatedAt': self.created_at,
            'UpdatedAt': self.updated_at,
            'MenuId': self.menu_id,
            'Carts': [cart.serialize for cart in self.carts],
            'Reservations': [reservation.serialize for reservation in self.reservations]
        }
