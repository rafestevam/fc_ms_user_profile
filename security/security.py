'''
Created on 9 de abr de 2020

@author: RAEO
'''
from models.models import User
from flask_jwt_extended.jwt_manager import JWTManager
from security.blacklist import BLACKLIST

def configure_jwt(app):
    jwt = JWTManager(app)
    
    @jwt.user_claims_loader
    def add_claims_to_jwt(identity):
        user = User.objects.get(username=identity)
        if user:
            role = ''
            if user.roles.admin:
                role = 'admin'
            if user.roles.superuser:
                role = 'superuser'
            if user.roles.collaborator:
                role = 'collaborator'
            
            return {
                'username': user.username,
                'name': user.name,
                'cellPhone': user.cellPhone,
                'active': user.active,
                'role': role
            }
            
    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(token):
        return token['jti'] in BLACKLIST
    
    
        
    
