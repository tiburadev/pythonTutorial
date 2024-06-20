from flask import jsonify

def get(status_code, message, data=None, success=False):
    # Define the mapping of status codes to meta types
    status_type_map = {
        200: "success",
        201: "created",
        204: "deleted",
        400: "Invalid Request",
        401: "Unauthorized Requests",
        403: "Forbidden",
        404: "Resource Not Found",
        500: "Server Issue"
    }
    
    meta_type = status_type_map.get(status_code, "Unknown")
    
    
    response = {
        "status": status_code,
        "message": meta_type,
        "data": [],
        "success": success
    }
    if(data):
      response['rows'] = len(data)
      response['data']=data

    return jsonify(response), status_code
