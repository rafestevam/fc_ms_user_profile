from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask.globals import request
from flask.json import jsonify
from mongoengine.errors import DoesNotExist, NotUniqueError
from models.user import User
from models.profile import Profile
from models.roles import Roles
from utils.responses import (
    resp_does_not_exist_err, 
    resp_exception_err,
    resp_data_invalid_err, 
    resp_user_updated, 
    resp_user_created, 
    resp_not_unique_err,
    resp_user_deleted
)
import uuid
import bcrypt

class UserResource(Resource):

    @jwt_required
    def get(self, guid):

        try:
            user = User.objects.get(guid=guid)

            return self.__to_json(user)
        
        except DoesNotExist:
            return resp_does_not_exist_err('Profiles', guid)
        
        except Exception as e:
            return resp_exception_err('Profiles', e.__str__())

    @jwt_required
    def put(self, guid):

        req_data = request.get_json() or None
        
        if req_data is None:
            return resp_data_invalid_err('Users', [])

        try:
            user = User.objects.get(guid=guid)
            User.objects.get(guid=guid).update(
                set__profile__name = req_data['profile']['name'],
                set__profile__avatar = req_data['profile']['avatar'],
                set__profile__cellPhone = req_data['profile']['cellPhone'],
                set__roles__admin = True if req_data['role'] == 'administrator' else False,
                set__roles__superuser = True if req_data['role'] == 'superuser' else False,
                set__roles__collaborator = True if req_data['role'] == 'collaborator' else False
            )

            return resp_user_updated('Users', user.username)

        except DoesNotExist:
            return resp_does_not_exist_err('Users', req_data['guid'])

        except Exception as ex: # pylint: disable=broad-except
            return resp_exception_err('Users', ex.__str__())

    @jwt_required
    def delete(self, guid):

        try:
            user = User.objects.get(guid=guid)
            User.objects.get(guid=guid).delete

            return resp_user_deleted('Users', user.username)
        
        except DoesNotExist:
            return resp_does_not_exist_err('Users', guid)

        except Exception as ex: # pylint: disable=broad-except
            return resp_exception_err('Users', ex.__str__())

    def __get_role(self, roles):
        if roles.admin:
            return 'administrator'
        if roles.superuser:
            return 'superuser'
        if roles.collaborator:
            return 'collaborator'
        
    def __to_json(self, user):
        prof = jsonify(
            name = user.profile.name,
            cellPhone = user.profile.cellPhone,
            avatar = user.profile.avatar
        )
        resp = jsonify(
            guid = user.guid,
            username = user.username,
            role = self.__get_role(user.roles),
            createdIn = user.createdIn,
            active = user.active,
            profile = prof.json
        )
        return resp.json