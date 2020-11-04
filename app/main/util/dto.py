from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='User related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='User Email address'),
        'username': fields.String(required=True, description='User Username'),
        'password': fields.String(required=True, description='User Password'),
        'public_id': fields.String(description='User Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='Authentication related operations')
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='The username'),
        'password': fields.String(required=True, description='The user password '),
    })


class BalanceDto:
    api = Namespace('balance', description='Branch Balances related operations')
    balance = api.model('balance_details', {
        'branch_id': fields.Integer(required=True, description='Branch Identifier'),
        'today_cash': fields.Integer(required=True, description='Today cash amount'),
        'tomorrow_cash': fields.Integer(required=False, description='Tomorrow cash amount'),
        'comments': fields.String(required=False, description='Balance comments'),
        'discount_day': fields.Boolean(required=False, description='Discount day'),
        'date': fields.Boolean(required=False, description='Balance date')
    })
