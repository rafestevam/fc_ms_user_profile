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
from resources.userlist import Users
from resources.userresource import UserResource
from resources.queryuser import Available
from resources.activateuser import ActivateUser

def routing_api(url_prefix='', api=Api()):
#API Routing
    api.add_resource(Hello, url_prefix + '/hello')
    api.add_resource(SignUp, url_prefix + '/new')
    api.add_resource(SignIn, url_prefix + '/auth')
    api.add_resource(RefreshToken, url_prefix + '/auth/refresh')
    #api.add_resource(SignOut, url_prefix + '/logout')
    api.add_resource(Users, url_prefix + '/')
    api.add_resource(UserResource, url_prefix + '/<string:guid>')
    api.add_resource(ActivateUser, url_prefix + '/<string:guid>/active')
    api.add_resource(Available, url_prefix + '/available')
