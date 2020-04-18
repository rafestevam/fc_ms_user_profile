'''
Created on 17 de abr de 2020

@author: RAEO
'''
from db import mongo
from mongoengine.fields import (
    EmailField, 
    StringField, 
    DateTimeField, 
    BooleanField
)
from datetime import datetime
from mongoengine import EmbeddedDocumentField
from models.roles import Roles

class User(mongo.Document):
    
    meta = {'collection': 'users'}
    
    username = EmailField(unique=True, required=True)
    password = StringField(required=True)
    createdIn = DateTimeField(default=datetime.now)
    active = BooleanField(default=False)
    roles = EmbeddedDocumentField(Roles, default=Roles)
    
