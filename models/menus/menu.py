from app import db

class Menu(db.Model):
#    Representation of a menu

    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50))
    items = db.Column(db.String(50))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    owner_restaurant_name = db.Column(db.String(50), nullable=True)