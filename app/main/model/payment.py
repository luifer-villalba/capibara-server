import datetime
from app.main import db


class Payment(db.Model):
    """ Client Payment Model for storing business payments related details """
    __tablename__ = "payment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer)
    comments = db.Column(db.String)
    type = db.Column(db.String)
    date = db.Column(db.DateTime, nullable=False)
    balance_id = db.Column(db.Integer, db.ForeignKey('balance.id'))
    registered_on = db.Column(db.DateTime, nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
