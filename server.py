import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from app.routes import routes 
# from app.middlewares import token_required
import app.responses as responses
from app.database import db, migrate
from app.config import Config

load_dotenv()
app = Flask(__name__)
app.config['PORT'] = os.getenv('PORT', 5010)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
app.config.from_object(Config)

@app.after_request
def apply_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept, Authorization, token, access-token"
    return response

@app.before_request
def before_request():
    print('Request Headers', request.headers)
    origin = request.headers.get('Origin')

# app.before_request()
app.register_blueprint(routes)

@app.errorhandler(404)
def page_not_found(e):
    return responses.get(404, "Invalid request", "Invalid!")

if __name__ == '__main__':
    app.run(debug=True, port=app.config['PORT'])
