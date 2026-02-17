from flask import Blueprint, session
from flask_jwt_extended import jwt_required,get_jwt_identity

api_route = Blueprint()

@api_route.route('/auth',methods = ['GET'])
def auth_dashboard():
    pass