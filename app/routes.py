from flask import Blueprint, request
from app import responses
routes = Blueprint('routes',__name__)
# import mysql.connector
from .controller import User
from flask import  jsonify

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Tibura2018!",
#   database="classicmodels"
# )

# mycursor = mydb.cursor()
@routes.route('/sample-route',methods=['GET'])
def sample_route():
    # mycursor.execute("CREATE TABLE python (name VARCHAR(255), address VARCHAR(255))")
    obj=User()
    data =obj.get_all_users()
    
    return responses.get(200,"Sucess",data,True)
@routes.route('/getOrders',methods=['GET'])
def getOrders():
    return  responses.get(200,"Sucess","i am getting Data",True)
@routes.route('/addUser',methods=['POST'])
def addUser():
    obj=User()
    data =obj.add_user(request.json)
    return data
   