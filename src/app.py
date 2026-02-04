from flask import Flask, render_template,redirect, Blueprint,flash,jsonify
import os
from dotenv import load_dotenv
from flask_jwt_extended import create_access_token,get_jwt,jwt_required,JWTManager
from database.database import getConexion

from routes.auth import auth_route
from routes.profile import profile_route


app = Flask(__name__)
app.secret_key=os.getenv('SECRETKEY')
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')

app.register_blueprint(auth_route)
app.register_blueprint(profile_route)

@app.route('/')
def index():
    flash('Bienvenido')
    return render_template('index.html',title = 'Inicio')

@app.route('/about')
def about():
    return render_template('about.html',title = 'about')

@app.route('/healthz')
def healthz():
    try:
        conexion =getConexion()
        cursor = conexion.cursor()
        cursor.execute('SELECT 1')
        return jsonify({"status":"ok"})
    except Exception as e:
        return jsonify({"status":"error en la conexion {}".format(str(e))})
        


if __name__=='__main__':
    app.run(debug=True)