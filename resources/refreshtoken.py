'''
Created on 9 de abr de 2020

@author: RAEO
'''
from flask_restful import Resource
from flask_jwt_extended.view_decorators import jwt_refresh_token_required
from flask_jwt_extended.utils import get_jwt_identity, create_access_token

class RefreshToken(Resource):
    
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200