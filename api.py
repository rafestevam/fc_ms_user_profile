'''
Created on 8 de abr de 2020

@author: RAEO
'''
from resources.hello import Hello
from resources.signup import SignUp
from resources.signin import SignIn
from resources.refreshtoken import RefreshToken
from resources.signout import SignOut
from flask_restful import Api
from resources.users import Users
from resources.queryuser import QueryUser

def routing_api(url_prefix='', api=Api()):
#API Routing
    api.add_resource(Hello, url_prefix + '/hello')
    api.add_resource(SignUp, url_prefix + '/signup')
    api.add_resource(SignIn, url_prefix + '/signin')
    api.add_resource(RefreshToken, url_prefix + '/refresh')
    api.add_resource(SignOut, url_prefix + '/logout')
    api.add_resource(Users, url_prefix + '/')
    api.add_resource(QueryUser, url_prefix + '/query')
