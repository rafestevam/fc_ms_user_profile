'''
Created on 9 de abr de 2020

@author: RAEO
'''
from flask_restful import Resource
from flask_jwt import jwt_required
from flask_jwt_extended.utils import get_raw_jwt
from security.blacklist import BLACKLIST
from utils.responses import resp_user_loggedout

class SignOut(Resource):

    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti'] # Get the "JWT ID (JTI)" from the token
        BLACKLIST.add(jti)
        return resp_user_loggedout