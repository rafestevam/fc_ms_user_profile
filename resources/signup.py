# -*- coding:utf-8 -*-
'''
Created on 8 de abr de 2020

@author: RAEO
'''
from flask_restful import Resource
from flask.globals import request
from flask_jwt_extended import jwt_required
import bcrypt
from mongoengine.errors import NotUniqueError
from utils.responses import resp_not_unique_err, resp_data_invalid_err,\
    resp_user_created
from models.user import User
from models.profile import Profile
from models.roles import Roles

class SignUp(Resource):

    @jwt_required
    def post(self):
        
        req_data = request.get_json() or None
        
        if req_data is None:
            return resp_data_invalid_err('Users', [])
        
        try:
            User(
                username = req_data['username'],
                password = bcrypt.hashpw(req_data['password'].encode('utf-8'), bcrypt.gensalt()),
                profile = Profile(
                    name = req_data['profile']['name'],
                    cellPhone = req_data['profile']['cellPhone'],
                    avatar = req_data['profile']['avatar']
                ),
                roles = Roles(
                    admin = True if req_data['roles']['role_admin'] == 'true' else False, 
                    superuser = True if req_data['roles']['role_superuser'] == 'true' else False,
                    collaborator = True if req_data['roles']['role_collaborator'] == 'true' else False
                )
            ).save()
            
            return resp_user_created('Users', req_data['username'])
        except NotUniqueError:
            return resp_not_unique_err('Users', 'usuário')
        
        