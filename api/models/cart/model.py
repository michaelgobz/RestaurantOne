"""cart model"""


from datetime import datetime

from api.core.base import declarative_base as db


class Cart(db.Model):
    """cart database model"""
    __tablename__ = 'Carts'

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id'), nullable=False)
    items = db.relationship('CartItem', backref='cart', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(),
                           onupdate=datetime.utcnow())

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'items': [item.serialize for item in self.items]
        }


class CartItem(db.Model):
    """cart items database model"""
    __tablename__ = 'CartItems'

    id = db.Column(db.String(50), primary_key=True)
    cart_id = db.Column(db.String(50), db.ForeignKey('carts.id'), nullable=False)
    menu_item_id = db.Column(db.String(50), db.ForeignKey('menu_items.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    # json serialization
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'Id': self.id,
            'CartId': self.cart_id,
            'item': self.menu_item_id,
            'Price': self.price,
            'Quantity': self.quantity
        }