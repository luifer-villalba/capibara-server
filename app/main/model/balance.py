import datetime
from app.main import db


class Balance(db.Model):
    """ Balance Model for storing business cash balance related details """
    __tablename__ = "balance"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    branch = db.Column(db.Integer, db.ForeignKey('branch.id'))
    today_cash = db.Column(db.Integer)
    tomorrow_cash = db.Column(db.Integer, nullable=True)
    cash_list = db.relationship("Cash")
    cancelled_invoice_list = db.relationship("CancelledInvoice")
    payment_list = db.relationship("Payment")
    expense_list = db.relationship("Expense")
    # todo: calculo de ventas (pre-insert)
    calculated_sales = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(), nullable=True)
    discount_day = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime, nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
