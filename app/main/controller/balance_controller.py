from flask import request
from flask_restplus import Resource

from ..util.decorator import token_required
from ..util.dto import BalanceDto
from ..service.balance_service import get_all_balances

api = BalanceDto.api
_balance = BalanceDto.balance


@api.route('/')
class BalanceList(Resource):
    @api.doc('list_of_branch_balances')
    @api.marshal_list_with(_balance, envelope='data')
    @token_required
    def get(self):
        """List all saved balances"""
        return get_all_balances()
