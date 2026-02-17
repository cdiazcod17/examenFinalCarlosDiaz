from flask import redirect,render_template,Blueprint,session,request,flash,url_for
from flask_jwt_extended import jwt_required,get_jwt_identity    
from werkzeug.security import generate_password_hash,check_password_hash
from database.database import getConexion


profile_route = Blueprint('profile_route',__name__)


@profile_route.route('/profile' , methods=['GET'])
#@jwt_required()
def profile():
    #current_user = get_jwt_identity()  
    if not 'user_id' in session:
        return redirect(url_for('auth_route.login_form'))  
    
    user_id =session['user_id']
    conexion = getConexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute('''
        SELECT c.name, 
               c.gender, 
               c.image_url as imagen 
        FROM characters_fav c 
        INNER JOIN characters_saved cs ON c.id = cs.character_id 
        WHERE cs.user_id = %s
    ''', (user_id,))
    characters = cursor.fetchall() 
    data = {
        "title":"profile",
        "characters":characters
    }   
    return render_template('profile.html',data = data)
