from flask_restful import Resource
from flask_jwt import jwt_required
from flask.globals import request
from utils.responses import resp_data_invalid_err, resp_user_already_exists_err, resp_user_created
from models.user import User
from mongoengine.errors import DoesNotExist

class QueryUser(Resource):

    @jwt_required
    def post(self):
        req_data = request.get_json() or None

        if req_data is None:
            return resp_data_invalid_err('Users', [])

        try:
            user = User.objects.get(username=req_data['username'])

            if user:
                return resp_user_already_exists_err('User', user)
        
        except DoesNotExist:
            return { 
                'message': 'username available'
            }, 200