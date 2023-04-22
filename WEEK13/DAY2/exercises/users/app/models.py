from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    street = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zipcode = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(10), default="client")

