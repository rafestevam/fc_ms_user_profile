'''
Created on 8 de abr de 2020

@author: RAEO
'''
from flask.app import Flask
from flask_cors.extension import CORS
from flask_restful import Api
from api import routing_api
from db import mongo as mongo
from utils.createadminuser import CreateAdminUser
from utils.createdir import CreateDir
from security.security import configure_jwt
from configs import config

app = Flask(__name__, static_folder=config.UPLOAD_DIR, static_url_path='/static/profile')
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config.from_object(config)
api = Api(app)

routing_api(url_prefix='/users', api=api)

configure_jwt(app)
mongo.init_app(app)

with app.app_context():
    CreateDir.image_dir(app.config['UPLOAD_DIR'])
    CreateAdminUser.create()


if __name__ == '__main__':
    app.run()
    #app.run(debug=True)
    #app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)
