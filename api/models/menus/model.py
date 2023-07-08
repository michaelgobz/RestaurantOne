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
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'restaurant_id': self.restaurant_id,
            'items': [item.serialize for item in self.items],
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
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'foods': self.foods,
            'category': self.category,
            'price': self.price,
            'isAvailable': self.is_available,
            'isDeliverable': self.is_deliverable,
            'rating': self.rating,
            'duration': self.duration_of_preparation,
            'avatar': self.avatar,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'menu_id': self.menu_id,
            'carts': [cart.serialize for cart in self.carts],
            'reservations': [reservation.serialize for reservation in self.reservations]
        }
