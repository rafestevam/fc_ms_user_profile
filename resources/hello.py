'''
Created on 8 de abr de 2020

@author: RAEO
'''
from flask_restful import Resource

class Hello(Resource):
    
    def get(self):
        return {"message": "You are here!"}

    