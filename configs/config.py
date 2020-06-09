# -*- coding: utf-8 -*-
'''
Created on 7 de abr de 2020

@author: RAEO
'''
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_DIR = '{}/profiles/'.format(BASEDIR)
SECRET_KEY = 'fc-collab'
CORS_HEADERS = 'Content-Type'
JWT_SECRET_KEY = 'fc-collab'
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
PROPAGATE_EXCEPTIONS = True
# MONGO_URI = 'mongodb://mongoadmin:c4d31r4@cluster-fc-shard-00-00-cqclf.gcp.mongodb.net:27017,cluster-fc-shard-00-01-cqclf.gcp.mongodb.net:27017,cluster-fc-shard-00-02-cqclf.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster-FC-shard-0&authSource=admin&retryWrites=true&w=majority'
# MONGO_DB = 'fc_database'
MONGODB_SETTINGS = {
#    'db': 'fc-database',
    'host': 'mongodb://mongoadmin:c4d31r4@cluster-fc-shard-00-00-cqclf.gcp.mongodb.net:27017,cluster-fc-shard-00-01-cqclf.gcp.mongodb.net:27017,cluster-fc-shard-00-02-cqclf.gcp.mongodb.net:27017/fc_database?ssl=true&replicaSet=Cluster-FC-shard-0&authSource=admin&retryWrites=true&w=majority',
}
FC_ADMIN_USER = 'admin@fc-collab.com'
FC_ADMIN_PASS = 'manage'
