from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask.globals import request
from utils.responses import resp_data_invalid_err, resp_user_already_exists_err, resp_exception_err
from models.user import User
from mongoengine.errors import DoesNotExist

class Available(Resource):

    @jwt_required
    def post(self):
        # return "success", 200
        req_data = request.get_json() or None

        print(req_data)
        if req_data is None:
            return resp_data_invalid_err('Users', [])

        try:
            user = User.objects.get(username=req_data['username'])

            if user:
                return resp_user_already_exists_err('User', user)
                
        except DoesNotExist:
            return {
                       'message': 'Usuário disponível'
                   }, 200

        except Exception as ex: # pylint: disable=broad-except
            return resp_exception_err('Users', ex.__str__())
