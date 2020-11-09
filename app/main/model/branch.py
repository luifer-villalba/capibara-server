from app.main import db


class Branch(db.Model):
    """ Branch Model for storing business branch related details """
    __tablename__ = "branch"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(255), unique=False, nullable=False)
    description = db.Column(db.String(255), unique=False, nullable=False)
    address = db.Column(db.String(255), unique=False, nullable=False)
    balance_list = db.relationship("Balance")
    checkin_list = db.relationship("UserCheckin")
