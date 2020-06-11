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
from utils.responses import ( 
    resp_not_unique_err, 
    resp_data_invalid_err,
    resp_user_created, 
    resp_exception_err
)
from utils.createdir import CreateDir
from models.user import User
from models.profile import Profile
from models.roles import Roles
from configs import config
import uuid
import os

class SignUp(Resource):

    @jwt_required
    def post(self):
        if request.form is None:
            return resp_data_invalid_err('Users', [])

        try:
            unique_guid = str(uuid.uuid4())
            initial_pwd = 'Rckb1000!'
            img_file = request.files['imageFile']
            if img_file:
                file_ext = img_file.filename.rsplit('.', 1)[1].lower()
                filename = '{}.{}'.format(unique_guid, file_ext)
                img_file.save(os.path.join(config.UPLOAD_DIR, filename))

            User(
                guid = unique_guid,
                username = request.form['username'],
                active = True if request.form['active'] == 'true' else False,
                password = bcrypt.hashpw(initial_pwd.encode('utf-8'), bcrypt.gensalt()),
                profile = Profile(
                    name = request.form['profile.name'],
                    cellPhone = request.form['profile.cellPhone'],
                    avatar = filename
                ),
                roles = Roles(
                    admin = True if request.form['role'] == 'administrator' else False, 
                    superuser = True if request.form['role'] == 'superuser' else False,
                    collaborator = True if request.form['role'] == 'collaborator' else False
                )
            ).save()
            
            return resp_user_created('Users', request.form['username'])

        except NotUniqueError:
            return resp_not_unique_err('Users', 'usuário')
        
        except Exception as ex: # pylint: disable=broad-except
            return resp_exception_err('Users', ex.__str__())

    # @jwt_required
    # def post(self):
        
    #     req_data = request.get_json() or None
        
    #     if req_data is None:
    #         return resp_data_invalid_err('Users', [])
        
    #     try:
    #         unique_guid = str(uuid.uuid4())
    #         User(
    #             guid = unique_guid,
    #             username = req_data['username'],
    #             password = bcrypt.hashpw(req_data['password'].encode('utf-8'), bcrypt.gensalt()),
    #             profile = Profile(
    #                 name = req_data['profile']['name'],
    #                 cellPhone = req_data['profile']['cellPhone'],
    #                 avatar = req_data['profile']['avatar']
    #             ),
    #             roles = Roles(
    #                 admin = True if req_data['role'] == 'administrator' else False, 
    #                 superuser = True if req_data['role'] == 'superuser' else False,
    #                 collaborator = True if req_data['role'] == 'collaborator' else False
    #             )
    #         ).save()
            
    #         return resp_user_created('Users', req_data['username'])

    #     except NotUniqueError:
    #         return resp_not_unique_err('Users', 'usuário')
        
    #     except Exception as ex: # pylint: disable=broad-except
    #         return resp_exception_err('Users', ex.__str__())
        
        