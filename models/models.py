'''
Created on 8 de abr de 2020

@author: RAEO
'''
from db import mongo
from mongoengine.fields import StringField, DateTimeField, BooleanField,\
    EmailField
from datetime import datetime
from mongoengine import EmbeddedDocument, EmbeddedDocumentField

class Roles(EmbeddedDocument):
    
    admin = BooleanField(default=False)
    superuser = BooleanField(default=False)
    collaborator = BooleanField(default=True)
    
    
class User(mongo.Document):
    
    meta = {'collection': 'users'}

    username = EmailField(unique=True, required=True)
    password = StringField(required=True)
    name = StringField(default='')
    cellPhone = StringField(default='')
    createdIn = DateTimeField(default=datetime.now)
    active = BooleanField(default=False)
    roles = EmbeddedDocumentField(Roles, default=Roles)
    
    
        