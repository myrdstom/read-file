from app.uploads import apca_v1
from flask import Flask, jsonify
from Instance.config import DevelopmentConfig
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    CORS(app)

    @app.errorhandler(404)
    def not_found(e):
        response = jsonify({'message': 'The requested Resource does not exist; Please review the URL'})
        response.status_code = 404
        return response

    app.register_blueprint(apca_v1)

    return app
