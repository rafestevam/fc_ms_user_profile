from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import url_for
from configs import config
import os

class Image(Resource):

    # @jwt_required
    def get(self, guid):

        filename = '{}.jpg'.format(guid)
        full_filename = os.path.join(config.UPLOAD_DIR, filename)
        url_image = url_for('static', filename=full_filename)
        return {"imagePath": url_image}, 200
        # return send_file(full_filename, mimetype='image/*')