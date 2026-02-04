from flask import redirect,render_template,Blueprint,session,request,flash,url_for
from flask_jwt_extended import create_access_token,get_jwt,jwt_required
from werkzeug.security import generate_password_hash,check_password_hash
from database.database import getConexion


auth_route = Blueprint('auth_route',__name__)

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
    
    if not  email or not password:
        flash('Todos los datos son requeridos','danger')
        return redirect(url_for('auth_route.login'))
        
    try:
        conexion = getConexion()
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM users WHERE email = %s',(email,))
        user = cursor.fetchone()
        if not user:
            flash('usuario no existe por favor verifique los datos','danger')
            return redirect(url_for('auth_route.login'))        
        
        if not user:
            flash('usuario no existe por favor verifique los datos','danger')
            return redirect(url_for('auth_route.login'))    
        
        if not check_password_hash(user['password_hash'],password):
            flash('usuario no existe por favor verifique los datos','danger')
            return redirect(url_for('auth_route.login')) 
        
        data = {"user_id":user['id'],"email":"email"}
        token = create_access_token(identity=data)
        
        session['user_id'] = user['id']
        session['email'] = user['email']
        session['rol'] = user['rol']
        session['token'] = token
        flash('Bienvenido {}'.format(user['username']),'success')
        return render_template('/profile.html',data=data)
        
    except Exception as e:
        flash('Error en la peticion, por favor intente nuevamente {}'.format(str(e)),'danger')
        return redirect(url_for('auth_route.login')) 
    finally:
        if conexion:
            conexion.close()
            
@auth_route.route('/login',methods=['GET'])
def login():
    
    return render_template('login.html',title = 'login')
   

@auth_route.route('/logout')
def logout():
    session.clear()
    flash('Logout exitoso','success')
    return redirect(url_for('auth_route.login'))