'''
Created on 17 de abr de 2020

@author: RAEO
'''
from mongoengine import EmbeddedDocument
from mongoengine.fields import BooleanField

class Roles(EmbeddedDocument):
    
    admin = BooleanField(default=False)
    superuser = BooleanField(default=False)
    collaborator = BooleanField(default=True)