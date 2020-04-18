'''
Created on 8 de abr de 2020

@author: RAEO
'''
from flask.app import Flask
from db import mongo  
from utils.createadminuser import CreateAdminUser
from security.security import configure_jwt
from flask_cors.extension import CORS
from configs import config
from flask_restful import Api
from api import routing_api

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config.from_object(config)
api = Api(app)

routing_api(url_prefix='/user', api=api)

configure_jwt(app)
mongo.init_app(app)

with app.app_context():
    CreateAdminUser.create()

if __name__ == '__main__':
    app.run(debug=True)