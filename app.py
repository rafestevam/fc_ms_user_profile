'''
Created on 8 de abr de 2020

@author: RAEO
'''
from flask.app import Flask
from api import api_bp
from db import mongo  
from utils.createadminuser import CreateAdminUser
from security.security import configure_jwt
from flask_cors.extension import CORS

def create_app(config_filename):
    app = Flask(__name__)
    cors = CORS(app, resources={r"*": {"origins": "*"}})
    app.config.from_object(config_filename)
    
    app.register_blueprint(api_bp, url_prefix='/users')
    
    mongo.init_app(app)
    
    with app.app_context():
        CreateAdminUser.create()
    
    return app

if __name__ == '__main__':
    app = create_app("configs.config")
    configure_jwt(app)
    app.run(debug=True)