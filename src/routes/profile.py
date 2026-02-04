from flask import redirect,render_template,Blueprint,session,request,flash,url_for
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash,check_password_hash
from database.database import getConexion
import requests

profile_route = Blueprint('profile_route',__name__)

API = 'https://futuramaapi.com/api/characters'

response = requests.get(API)
characters = response.json()

list_user= []
list = [x for x in range(5)]

@profile_route.route('/profile' , methods=['GET'])
def profile():
    return redirect(url_for('profile.html',title = 'profile'))
    