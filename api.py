'''
Created on 8 de abr de 2020

@author: RAEO
'''
from flask.blueprints import Blueprint
from flask_restful import Api
from resources.hello import Hello
from resources.signup import SignUp
from resources.signin import SignIn
from resources.refreshtoken import RefreshToken
from resources.signout import SignOut

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#API Routing
api.add_resource(Hello, '/hello')
api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(RefreshToken, '/refresh')
api.add_resource(SignOut, '/logout')
