from app import db

class Reservation(db.Model):
    """
    Initialize a Reservation instance
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.DateTime, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    nb_of_person = db.Column(db.Integer, nullable=False)
    additional_info = db.Column(db.Text)
    tables = db.Column(db.Integer)
    category = db.Column(db.String(50))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    tax = db.Column(db.Integer, nullable=False)
    menu_item = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self):
        """ Initialize Reservation instance
        """
        pass