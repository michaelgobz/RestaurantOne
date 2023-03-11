from app import db

class Reservation(db.Model):
 #   Representation of a reservation

    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text, nullable=True)
    duration = db.Column(db.DateTime, nullable=True)
    start = db.Column(db.DateTime, nullable=True)
    end = db.Column(db.DateTime, nullable=True)
    nb_of_person = db.Column(db.Integer, nullable=False, default=0)
    additional_info = db.Column(db.Text, nullable=True)
    tables = db.Column(db.Integer, nullable=True)
    category = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Integer, nullable=False, default=0)
    tax = db.Column(db.Integer, nullable=True)
    menu_item = db.Column(db.String(50), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)