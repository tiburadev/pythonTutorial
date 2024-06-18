from flask import jsonify

def get(status_code, message, data=None, success=True):
    return jsonify({
        "status": status_code,
        "message": message,
        "data": data,
        "success": success
    }), status_code