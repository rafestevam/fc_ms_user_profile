'''
Created on 17 de abr de 2020

@author: RAEO
'''
from db import mongo
from mongoengine.fields import EmailField, StringField

class Profile(mongo.Document):
    
    meta = {'collection': 'profiles'}
    
    username = EmailField(required=True)
    name = StringField(default='')
    cellPhone = StringField(default='')
    avatar = StringField(default='')