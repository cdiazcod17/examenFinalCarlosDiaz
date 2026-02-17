from flask import redirect,render_template,Blueprint,session,request,flash,url_for
from flask_jwt_extended import create_access_token,get_jwt,jwt_required
from werkzeug.security import generate_password_hash,check_password_hash
from database.get_database import getConexion
import random
from api.api_futurama import getCharacters


auth_route = Blueprint('auth_route',__name__)

def random_id():
    list = [ random.randint(1,427) for x in range(5) ]
    return list
    

@auth_route.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@auth_route.route('/register' , methods=['POST'])
def register_form():
    print(request.form.get('username'))
    username = request.form.get('username').strip().lower()
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    rol= request.form.get('rol')
    
    if not username or not email or not password or not confirm_password or not rol:
        flash('Todos los datos son requeridos','danger')
        return redirect(url_for('auth_route.register'))
        
    if password != confirm_password:
        flash('Todos los datos son requeridos','danger')
        return redirect(url_for('auth_route.register'))
    
    password_hash = generate_password_hash(password)
    
    try:
        conexion = getConexion()
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM users WHERE email = %s',(email,))
        user = cursor.fetchone()
        if user:
            flash('usuario ya registrado, por favor inicie sesion','danger')
            return redirect(url_for('auth_route.login'))     
        
        if rol == 'user':
            cursor.execute('INSERT INTO users (username,email,password_hash,rol) VALUES(%s,%s,%s,%s)',(username,email,password_hash,rol))
            conexion.commit()
            user_id = cursor.lastrowid
            list_characters = random_id()
            characters_insert = []
            fav_table = []
            
            for i in list_characters:
                character = getCharacters(i)
                tupla = (character['id'],
                        character['name'],
                        character['gender'],
                        character['image'])
                characters_insert.append(tupla)
                
                fav_table.append((user_id,character['id']))
        
            print(characters_insert)
            print(fav_table)
            query_characters='INSERT INTO characters_fav (id,name,gender,image_url) VALUES(%s,%s,%s,%s)'
            cursor.executemany(query_characters,characters_insert)
            conexion.commit()  
            
            query_characetrs_saved = 'INSERT INTO characters_saved (user_id,character_id) VALUES(%s,%s)'
            cursor.executemany(query_characetrs_saved,fav_table)
            conexion.commit()    
        
            flash('Registro realizado correctamente, por favor inicie sesion','danger')
            return redirect(url_for('auth_route.login_form'))
        
        if rol == 'admin':
            cursor.execute('INSERT INTO users (username,email,password_hash,rol) VALUES(%s,%s,%s,%s)',(username,email,password_hash,rol))
            conexion.commit()
            flash('Registro realizado correctamente, por favor inicie sesion','danger')
            return redirect(url_for('auth_route.login_form'))
        
    except Exception as e:
        flash('Ha ocurrido un error {}'.format(str(e)),'danger')
        return redirect(url_for('auth_route.register')) 
    finally:
        if conexion:
            conexion.close()


@auth_route.route('/login',methods=['POST'])
def login_form():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        flash('Todos los datos son requeridos','danger')
        return redirect(url_for('auth_route.login'))
        
    try:
        conexion = getConexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE email = %s',(email,))
        user = cursor.fetchone()

        if not user:
            flash('usuario no existe por favor verifique los datos','danger')
            return redirect(url_for('auth_route.login'))        
        
        if user and not check_password_hash(user['password_hash'],password):
            flash('Verifique la contrasena ingresada','danger')
            return redirect(url_for('auth_route.login'))    

        if not check_password_hash(user['password_hash'],password):
            flash('usuario no existe por favor verifique los datos','danger')
            return redirect(url_for('auth_route.login')) 

        data = {"user_id":user['id'],"email":email}
        token = create_access_token(identity=data)
        
        session['user_id'] = user['id']
        session['email'] = user['email']
        session['rol'] = user['rol']
        
        if user['rol'] == 'user': 
            flash('Bienvenido {}'.format(user['username']),'success')
            return redirect(url_for('profile_route.profile'))
        
        if user['rol'] == 'admin': 
            flash('Bienvenido {}'.format(user['username']),'success')
            return redirect(url_for('auth_route.auth_dashboard'))
        
    except Exception as e:
        print(e)
        flash('Error en la peticion, por favor intente nuevamente {}'.format(str(e)),'danger')
        return redirect(url_for('auth_route.login')) 
    finally:
        if conexion:
            conexion.close()
            
@auth_route.route('/login',methods=['GET'])
def login():
    if 'rol' not in session:
        return render_template('login.html',title = 'login')        
        
    if session['rol'] == 'user':
        return redirect(url_for('profile_route.profile') ) 
    
    if session['rol'] == 'admin':
        return redirect(url_for('auth_route.auth_dashboard') ) 
    

@auth_route.route('/logout')
def logout():
    session.clear()
    flash('Logout exitoso','danger')
    return redirect(url_for('index'))

@auth_route.route('/auth',methods = ['GET'])
def auth_dashboard():
    
    if not 'rol' in session:
        return redirect(url_for('auth_route.login'))
    
    if session['rol'] == 'user':
        flash('Acceso no autorizado','danger')
        return redirect(url_for('profile_route.profile'))
    return render_template('admin.html')