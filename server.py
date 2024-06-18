import os
from flask import Flask,request,jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from routes import routes

load_dotenv()

app=Flask(__name__)
app.config['PORT']= os.getenv('PORT',5010)
CORS(app,resources={r"/*":{"origins":"*"}},supports_credentials=True)
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
def verify_middleware():
    pass   
app.before_request(verify_middleware) 

app.register_blueprint(routes)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Invalid request", "message": "Invalid!"}), 404
if __name__=='__main__' :
    app.run(debug=True,port=app.config['PORT'])
