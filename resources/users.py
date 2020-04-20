'''
Created on 17 de abr de 2020

@author: RAEO
'''
from flask_restful import Resource
from mongoengine import DoesNotExist
from utils.responses import resp_does_not_exist_err, resp_exception_err
from flask_jwt_extended.view_decorators import jwt_required
from flask_jwt_extended.utils import get_jwt_identity
from models.user import User
from flask.json import jsonify


class Users(Resource):
    
    @jwt_required
    def get(self):
        
        userName = get_jwt_identity()
        try:
            return self.__to_json(User.objects.get(username=userName)), 200
        
        except DoesNotExist:
            return resp_does_not_exist_err('Profiles', userName)
        
        except Exception as e:
            return resp_exception_err('Profiles', e.__str__())
    
    @jwt_required
    def post(self):
        
        try:
            return [self.__to_json(user) for user in User.objects], 200
        
        except DoesNotExist:
            return resp_does_not_exist_err('Profiles', 'no_data')
        
        except Exception as e:
            return resp_exception_err('Profiles', e.__str__())
    
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
            username = user.username,
            role = self.__get_role(user.roles),
            createdIn = user.createdIn,
            active = user.active,
            profile = prof.json
        )
        return resp.json
        
        
    
            
        
        