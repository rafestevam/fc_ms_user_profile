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
from configs import config
import uuid
import bcrypt
import os, stat

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

        if request.form is None:
            return resp_data_invalid_err('Users', [])

        try:
            img_file = request.files['imageFile']
            if img_file:
                file_ext = img_file.filename.rsplit('.', 1)[1].lower()
                filename = '{}.{}'.format(guid, file_ext)
                img_file.save(os.path.join(config.UPLOAD_DIR, filename))

            user = User.objects.get(guid=guid)
            User.objects.get(guid=guid).update(
                set__profile__name = request.form['profile.name'],
                set__profile__avatar = filename,
                set__profile__cellPhone = request.form['profile.cellPhone'],
                set__roles__admin = True if request.form['role'] == 'administrator' else False,
                set__roles__superuser = True if request.form['role'] == 'superuser' else False,
                set__roles__collaborator = True if request.form['role'] == 'collaborator' else False
            )

            return resp_user_updated('Users', user.username)

        except DoesNotExist:
            return resp_does_not_exist_err('Users', guid)

        except Exception as ex: # pylint: disable=broad-except
            return resp_exception_err('Users', ex.__str__())

    @jwt_required
    def delete(self, guid):

        try:
            user = User.objects.get(guid=guid)
            User.objects.get(guid=guid).delete()

            if (os.path.exists(os.path.join(config.UPLOAD_DIR, user.profile.avatar))):
                os.remove(os.path.join(config.UPLOAD_DIR, user.profile.avatar))

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