import datetime
from app.main import db


class Cash(db.Model):
    """ Cash Model for storing business cash related details """
    __tablename__ = "cash"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    balance_id = db.Column(db.Integer, db.ForeignKey('balance.id'))
    registered_on = db.Column(db.DateTime, nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
