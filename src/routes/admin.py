from flask import Blueprint, session,request,jsonify
from flask_jwt_extended import jwt_required,get_jwt_identity
from database.database import getConexion
from werkzeug.security import generate_password_hash, check_password_hash

api_route = Blueprint('api_route',__name__,url_prefix='/api/admin')

@api_route.route('/',methods = ['GET'])
@jwt_required()
def get_admins():
    conexion = None
    try:
        conexion = getConexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE rol = 'admin'")
        admin = cursor.fetchall()
        if not admin:
            return jsonify({"message": "admins no encontrados"}), 404
        
        return jsonify({"data":admin})
        
    except Exception as e:
        return jsonify({"error":str(e)})
    finally:
        if conexion:
            conexion.close()
    
@api_route.route('/<int:id>',methods = ['GET'])
@jwt_required()
def get_admin(id):
    conexion = None
    try:
        conexion = getConexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s AND rol = 'admin'",(id,))
        admin = cursor.fetchone()
        if not admin:
            return jsonify({"message": "admin no encontrado"}), 404
        
        return jsonify({"data":admin})
        
    except Exception as e:
        return jsonify({"error":str(e)}),500
    finally:
        if conexion:
            conexion.close()

@api_route.route('/',methods = ['POST'])
@jwt_required()
def create_admin():
    conexion = None
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        
        if not username or not password or not confirm_password :
            return jsonify({"error":"Todos los datos son necesarios"}),400
        
        if password != confirm_password:            
            return jsonify({"error":"Las contrasenas no coinciden"}),400
    
        password_hash = generate_password_hash(password)        
        
        conexion = getConexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("INSERT INTO users (username,email,password_hash,rol) VALUES (%s,%s,%s,'admin') ",(username,email,password_hash))
        conexion.commit()
        
        return jsonify({"message": "Admin creado","id": cursor.lastrowid}), 201 
        
    except Exception as e:
        return jsonify({"error":str(e)}),500
    finally:
        if conexion:
            conexion.close()

@api_route.route('/<int:id>',methods = ['PUT'])
@jwt_required()
def update_admin(id):
    conexion = None
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        
        if not username or not email:
            return jsonify({"error":"Todos los datos son necesarios"}),400
        
        conexion = getConexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("UPDATE users set username = %s, email = %s WHERE id = %s AND rol = 'admin' ",(username,email,id))
        conexion.commit()
        
        return jsonify({"message": "Admin actualizado","id": cursor.lastrowid}), 201 
        
    except Exception as e:
        return jsonify({"error":str(e)}),500
    finally:
        if conexion:
            conexion.close()
            
@api_route.route('/<int:id>',methods = ['DELETE'])
@jwt_required()
def delete_admin(id):
    conexion = None
    try:
        conexion = getConexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("DELETE FROM users WHERE id = %s ",(id,))
        conexion.commit()
        
        return jsonify({"message": "Admin ELIMINADO"}), 200
        
    except Exception as e:
        return jsonify({"error":str(e)}),500
    finally:
        if conexion:
            conexion.close()
        