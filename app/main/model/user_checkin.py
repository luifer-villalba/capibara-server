import pytz
from datetime import datetime

from app.main import db


class UserCheckin(db.Model):
    """ UserCheckin Model for storing business staff marking related details """
    __tablename__ = "user_checkin"
    pytz.timezone('America/Asuncion').localize(datetime.now())

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
