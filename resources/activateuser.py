from flask_restful import Resource
from flask.globals import request
from flask_jwt_extended import jwt_required
from models.user import User
from utils.responses import (
    resp_user_updated,
    resp_does_not_exist_err,
    resp_data_invalid_err,
    resp_exception_err
)
from mongoengine.errors import DoesNotExist

class ActivateUser(Resource):

    @jwt_required
    def put(self, guid):

        req_data = request.get_json() or None
        
        if req_data is None:
            return resp_data_invalid_err('Users', [])

        try:
            user = User.objects.get(guid=guid)
            User.objects.get(guid=guid).update(
                active = req_data['active'],
            )

            return resp_user_updated('Users', user.username)

        except DoesNotExist:
            return resp_does_not_exist_err('Users', req_data['guid'])

        except Exception as ex: # pylint: disable=broad-except
            return resp_exception_err('Users', ex.__str__())