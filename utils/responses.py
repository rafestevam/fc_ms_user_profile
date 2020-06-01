'''
Created on 8 de abr de 2020

@author: RAEO
'''
from flask.json import jsonify
from utils.messages import (
    MSG_ALREADY_EXISTS, 
    MSG_INVALID_DATA, 
    MSG_SUCCESS,
    MSG_NOT_FOUND, 
    MSG_EXCEPTION, 
    MSG_INVALID_CREDENTIALS, 
    MSG_LOGGED_OUT,
    MSG_NOT_ACTIVE, 
    MSG_USER_ALREADY_EXISTS, 
    MSG_SUCCESS_UPD,
    MSG_SUCCESS_DEL
)
from models.user import User

def resp_not_unique_err(resource: str, description: str):
    '''
    Responses 400
    '''
    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string')
    
    resp = jsonify({
        'resource': resource,
        'message': MSG_ALREADY_EXISTS.format(description)
    })
    resp.status_code = 400
    
    return resp

def resp_data_invalid_err(resource: str, errors: dict):
    '''
    Responses 422 Unprocessable Entity
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')

    resp = jsonify({
        'resource': resource,
        'message': MSG_INVALID_DATA,
        'errors': errors,
    })

    resp.status_code = 422

    return resp

def resp_user_already_exists_err(resource: str, user: User):
    '''
    Responses 422 Unprocessable Entity
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')

    resp = jsonify({
        'resource': resource,
        'message': MSG_USER_ALREADY_EXISTS.format(user.username)
    })

    resp.status_code = 422

    return resp

def resp_does_not_exist_err(resource: str, description: str):
    '''
    Response 404 - Not Found
    '''
    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string')
    
    resp = jsonify({
        'resource': resource,
        'message': MSG_NOT_FOUND.format(description)
    })
    resp.status_code = 404
    
    return resp

def resp_not_active_err(resource: str, description: str):
    '''
    Response 401 - Unauthorized (Not Active)
    '''
    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string')
    
    resp = jsonify({
        'resource': resource,
        'message': MSG_NOT_ACTIVE.format(description)
    })
    resp.status_code = 401
    
    return resp

def resp_exception_err(resource: str, description: str):
    '''
    Response 404 - Not Found
    '''
    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string')
    
    resp = jsonify({
        'resource': resource,
        'message': MSG_EXCEPTION.format(description)
    })
    resp.status_code = 500
    
    return resp

def resp_invalid_credentials_err(resource: str):
    '''
    Response 401 - Not Authorized
    '''
    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string')
    
    resp = jsonify({
        'resource': resource,
        'message': MSG_INVALID_CREDENTIALS
    })
    resp.status_code = 401
    
    return resp

def resp_user_created(resource: str, description: str):
    '''
    Response 200 - OK
    '''
    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string')
    
    resp = jsonify({
        'resource': resource,
        'message': MSG_SUCCESS.format(description)
    })
    resp.status_code = 200
    
    return resp

def resp_user_updated(resource: str, description: str):
    '''
    Response 200 - OK
    '''
    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string')
    
    resp = jsonify({
        'resource': resource,
        'message': MSG_SUCCESS_UPD.format(description)
    })
    resp.status_code = 200
    
    return resp

def resp_user_deleted(resource: str, description: str):
    '''
    Response 200 - OK
    '''
    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string')
    
    resp = jsonify({
        'resource': resource,
        'message': MSG_SUCCESS_DEL.format(description)
    })
    resp.status_code = 200
    
    return resp

def resp_user_loggedout(resource: str):
    '''
    Response 200 - OK
    '''
    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string')
    
    resp = jsonify({
        'resource': resource,
        'message': MSG_LOGGED_OUT
    })
    resp.status_code = 200
    
    return resp
    