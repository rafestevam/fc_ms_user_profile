'''
Created on 9 de abr de 2020

@author: RAEO
'''
from flask_restful import Resource
from models.models import User
from flask.globals import request
from utils.responses import resp_data_invalid_err, resp_does_not_exist_err,\
    resp_exception_err, resp_invalid_credentials_err
from mongoengine import DoesNotExist
from flask_jwt_extended.utils import create_access_token, create_refresh_token
from bcrypt import checkpw

class SignIn(Resource):

    def post(self):
        req_data = request.get_json() or None
        
        if req_data is None:
            return resp_data_invalid_err('Users', [])
        
        try: 
            user = User.objects.get(username=req_data['username'])
            if user and checkpw(req_data['password'].encode('utf-8'), user.password.encode('utf-8')):
                access_token = create_access_token(identity=user.username, fresh=True)
                refresh_token = create_refresh_token(user.username)
                return {
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }, 200
            return resp_invalid_credentials_err('Users')
        
        except DoesNotExist:
            return resp_does_not_exist_err('Users', req_data['username'])
        
        except Exception as e:
            return resp_exception_err('Users', e.__str__())