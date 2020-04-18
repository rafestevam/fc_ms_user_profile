'''
Created on 17 de abr de 2020

@author: RAEO
'''
from flask_restful import Resource
from models.profile import Profile
from mongoengine import DoesNotExist
from utils.responses import resp_does_not_exist_err, resp_exception_err
from flask.json import jsonify
from flask_jwt_extended.utils import get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_required
    
class Profiles(Resource):
    
    @jwt_required
    def post(self):
        username = get_jwt_identity()
        
        try:
            profile = Profile.objects.get(username=username)
            return jsonify(profile), 200
        
        except DoesNotExist:
            return resp_does_not_exist_err('Profiles', username)
        
        except Exception as e:
            return resp_exception_err('Profiles', e.__str__())
    
    def get(self):
        
        try:
            profiles = [{"username": prof.username,
                         "name": prof.name,
                         "avatar": prof.avatar,
                         "cellPhone": prof.cellPhone} for prof in Profile.objects]
            return {"profiles": profiles}, 200
        
        except DoesNotExist:
            return resp_does_not_exist_err('Profiles', 'no_data')
        
        except Exception as e:
            return resp_exception_err('Profiles', e.__str__())
            
        
        