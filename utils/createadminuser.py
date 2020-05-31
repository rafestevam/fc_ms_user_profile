'''
Created on 8 de abr de 2020

@author: RAEO
'''
from configs.config import FC_ADMIN_USER, FC_ADMIN_PASS
import bcrypt
from models.user import User
from models.roles import Roles
from models.profile import Profile
import uuid

class CreateAdminUser():
    
    @staticmethod
    def create():
        try:
            hashed_pass = bcrypt.hashpw(FC_ADMIN_PASS.encode('utf-8'), bcrypt.gensalt())
            unique_guid = str(uuid.uuid4())
            User(
                guid = unique_guid,
                username = FC_ADMIN_USER, 
                password = hashed_pass, 
                active=True,
                roles=Roles(admin=True, collaborator=False, superuser=False),
                profile=Profile(name='Administrator', cellPhone='(99)99999-9999', avatar='')
            ).save()
            
        except Exception as e:
            pass
        