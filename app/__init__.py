# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.balance_controller import api as balance_ns

blueprint = Blueprint('api', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'authorization'
    }
}

api = Api(blueprint,
          title='Flask API WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service',
          authorizations=authorizations
          )

api.add_namespace(balance_ns, path='/balance')
api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
