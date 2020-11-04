import datetime
from app.main import db


class CancelledInvoice(db.Model):
    """ Cancelled Invoice Model for storing business invoice related details """
    __tablename__ = "cancelled_invoice"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    invoice_number = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    comments = db.Column(db.String)
    date = db.Column(db.DateTime, nullable=False)
    balance_id = db.Column(db.Integer, db.ForeignKey('balance.id'))
    registered_on = db.Column(db.DateTime, nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
