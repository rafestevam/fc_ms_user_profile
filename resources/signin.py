'''
Created on 9 de abr de 2020

@author: RAEO
'''
from flask_restful import Resource
from flask.globals import request
from utils.responses import resp_data_invalid_err, resp_does_not_exist_err,\
    resp_exception_err, resp_invalid_credentials_err, resp_not_active_err
from mongoengine import DoesNotExist
from flask_jwt_extended.utils import ( 
    create_access_token, 
    create_refresh_token,
    get_jwt_identity
)
from flask_jwt_extended import jwt_refresh_token_required
from bcrypt import checkpw
from models.user import User
import datetime

class SignIn(Resource):
    
    def post(self):
        req_data = request.get_json() or None
        
        if req_data is None:
            return resp_data_invalid_err('Users', [])
        
        try: 
            user = User.objects.get(username=req_data['username'])
            if checkpw(req_data['password'].encode('utf-8'), user.password.encode('utf-8')) is False:
                return resp_invalid_credentials_err('Users')
            if not user.active:
                return resp_not_active_err('Users', user.username)
            if user and checkpw(req_data['password'].encode('utf-8'), user.password.encode('utf-8')):
                expires = datetime.timedelta(seconds=3600)
                access_token = create_access_token(identity=user.guid, fresh=True, expires_delta=expires)
                refresh_token = create_refresh_token(user.guid)
                return {
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }, 200
            return resp_invalid_credentials_err('Users')
        
        except DoesNotExist:
            return resp_does_not_exist_err('Users', req_data['username'])
        
        except Exception as e:
            return resp_exception_err('Users', e.__str__())

# class TokenRefresh(Resource):
#     @jwt_refresh_token_required
#     def post (self):
#         current_user = get_jwt_identity()
#         new_token = create_access_token(identity=current_user, fresh=False)
#         return {'access_token': new_token}, 200