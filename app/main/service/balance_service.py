from app.main import db
from app.main.model.balance import Balance


def get_all_balances():
    return Balance.query.all()
