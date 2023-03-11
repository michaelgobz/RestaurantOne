from app import db

class Shipment(db.Model):
# Representation of a shipment

    __tablename__ = 'shipments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(250))
    capacity = db.Column(db.Integer)
    operator = db.Column(db.String(50))
    method = db.Column(db.String(50))
    means = db.Column(db.String(50))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)