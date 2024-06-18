from flask import Blueprint
routes = Blueprint('routes',__name__)

@routes.route('/sample-route')
def sample_route():
    return {"message": "This is a sample route"}
@routes.route('/getOrders')
def getOrders():
    return {"message": "I am getting Orders"}