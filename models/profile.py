'''
Created on 17 de abr de 2020

@author: RAEO
'''
from mongoengine.fields import StringField
from mongoengine import EmbeddedDocument

class Profile(EmbeddedDocument):

    name = StringField(default='')
    cellPhone = StringField(default='')
    avatar = StringField(default='')