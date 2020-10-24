import os
from app.uploads import apca_v1
import json
from flask_restful import Resource, Api

API = Api(apca_v1)


class Uploads(Resource):
    def get(self):
        with open("../menuItems.json", 'rb') as file:
            file_content = json.load(file)
        return file_content, 200


API.add_resource(Uploads, '/uploads')
