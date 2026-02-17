from flask import Blueprint, session,request,jsonify
from flask_jwt_extended import jwt_required,get_jwt_identity
from database.database import getConexion

api_route = Blueprint('api_route',__name__,url_prefix='/api/admin')

@api_route.route('/',methods = ['GET'])
@jwt_required()
def get_admins():
    try:
        conexion = getConexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE rol = 'admin'")
        admins = cursor.fetchall()
        
        return jsonify({"admins":admins})
        
    except Exception as e:
        return jsonify({"error":str(e)})
        