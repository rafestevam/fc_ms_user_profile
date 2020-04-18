'''
Created on 9 de abr de 2020

@author: RAEO
'''
from flask_jwt_extended.jwt_manager import JWTManager
from security.blacklist import BLACKLIST
from models.user import User
from flask.json import jsonify
from utils.messages import MSG_NO_TOKEN_AT_ALL, MSG_INVALID_TOKEN,\
    MSG_EXPIRED_TOKEN

def configure_jwt(app):
    jwt = JWTManager(app)
    
    @jwt.user_claims_loader
    def add_claims_to_jwt(identity):
        user = User.objects.get(username=identity)
        if user:
            role = ''
            if user.roles.admin:
                role = 'administrator'
            if user.roles.superuser:
                role = 'superuser'
            if user.roles.collaborator:
                role = 'collaborator'
            
            return {
                'username': user.username,
                'active': user.active,
                'role': role
            }
            
    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(token):
        return token['jti'] in BLACKLIST
    
    @jwt.unauthorized_loader
    def check_no_token(error):
        resp = jsonify({
            'error': 'no_token_at_all',
            'message': MSG_NO_TOKEN_AT_ALL
        })
        resp.status_code = 401
        
        return resp
    
    @jwt.invalid_token_loader
    def invalid_token(error):
        resp = jsonify({
            'error': 'invalid_token',
            'message': MSG_INVALID_TOKEN
        })
        resp.status_code = 401
        
        return resp
    
    @jwt.expired_token_loader
    def expired_token(error):
        resp = jsonify({
            'error': 'expired_token',
            'message': MSG_EXPIRED_TOKEN
        })
        resp.status_code = 401
        
        return resp
    
    
        
    
