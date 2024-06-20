from functools import wraps
import jwt
from flask import request,abort,current_app
from app import responses

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            # return  responses.get(401,"Authentication Token is missing!",None,True)
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401    
        try:
         data=jwt.decode(token,current_app.config["SECRET_KEY"],algorithms=["HS256"]) 
         print(data)
        except Exception as e:
           return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500
        
        return f(*args, **kwargs)

    return decorated