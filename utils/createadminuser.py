'''
Created on 8 de abr de 2020

@author: RAEO
'''
from configs.config import FC_ADMIN_USER, FC_ADMIN_PASS
import bcrypt
from models.user import User
from models.roles import Roles
from models.profile import Profile

class CreateAdminUser():
    
    @staticmethod
    def create():
        try:
            hashed_pass = bcrypt.hashpw(FC_ADMIN_PASS.encode('utf-8'), bcrypt.gensalt())
            User(
                username = FC_ADMIN_USER, 
                password = hashed_pass, 
                active=True,
                roles=Roles(admin=True, collaborator=False, superuser=False),
                profile=Profile(name='Administrator', cellPhone='(99)99999-9999', avatar='assets/avatars/profiles/avatar-3.jpg')
            ).save()
            
        except Exception as e:
            pass
        