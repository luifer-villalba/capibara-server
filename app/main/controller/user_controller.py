from flask import request
from flask_restplus import Resource

from ..service.auth_helper import Auth
from ..util.dto import UserDto, UserCheckinDto
from ..util.decorator import admin_token_required, token_required
from ..service.user_service import save_new_user, get_all_users, get_a_user, save_checkin, get_checkin_list

api = UserDto.api
_user = UserDto.user
_user_checkin = UserCheckinDto.user


@api.route('/')
class UserList(Resource):
    @admin_token_required
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User"""
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>/checkin/<branch_id>')
@api.doc(security='apikey')
@api.response(404, 'User not found.')
class UserCheckin(Resource):
    @token_required
    @api.marshal_with(_user_checkin)
    def post(self, public_id, branch_id):
        """Save personnel marking in the branch"""
        return save_checkin(public_id)


@api.route('/<public_id>/checkin-list')
@api.doc(security='apikey')
@api.response(404, 'User not found.')
class UserCheckinList(Resource):
    @token_required
    @api.marshal_with(_user_checkin)
    def get(self, public_id):
        """Get user checkin history"""
        return get_checkin_list(public_id)


@api.route('/<public_id>')
@api.response(404, 'User not found.')
class User(Resource):
    @api.marshal_with(_user)
    def get(self, public_id):
        """Get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
