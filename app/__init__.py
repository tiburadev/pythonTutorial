import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from app import routes
from .middlewares import token_required
from .database import db, migrate
from .config import Config


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['PORT'] = os.getenv('PORT', 5010)
    app.config.from_object(Config)

    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    @app.after_request
    def apply_cors(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = (
            "Origin, X-Requested-With, Content-Type, Accept, Authorization, token, access-token"
        )
        return response

    @app.before_request
    def before_request():
        print('Request Headers', request.headers)
        origin = request.headers.get('Origin')

    app.before_request(token_required)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(routes)

    # @app.errorhandler(404)
    # def page_not_found(e):
    #     return responses.get(404, "Invalid request", "Invalid!")

    return app
