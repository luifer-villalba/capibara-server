import uuid
import pytz
from datetime import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.user_checkin import UserCheckin


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    pytz.timezone('America/Asuncion').localize(datetime.now())
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.now()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please log in.'
        }
        return response_object, 409


def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        print(e)
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def get_checkin_list(public_id):
    user = get_a_user(public_id)
    return user.checkin_list


def save_checkin(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    pytz.timezone('America/Asuncion').localize(datetime.now())
    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please log in.'
        }
        return response_object, 409
    else:
        user_checkin = UserCheckin(
            staff_id=user.id
        )
        save_changes(user_checkin)
        return user_checkin
