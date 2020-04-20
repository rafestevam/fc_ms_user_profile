'''
Created on 17 de abr de 2020

@author: RAEO
'''
from mongoengine.fields import BooleanField
from mongoengine import EmbeddedDocument

class Roles(EmbeddedDocument):
    
    admin = BooleanField(default=False)
    superuser = BooleanField(default=False)
    collaborator = BooleanField(default=True)