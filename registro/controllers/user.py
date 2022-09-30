from registro import app
from flask_bcrypt import Bcrypt
from flask import request,flash,render_template,redirect,session 
from registro.models.user import User


bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("registro.html")

@app.route('/register/user', methods=['POST'])
def register():
    # validar el formulario aquí...

    # crear el hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # poner pw_hash en el diccionario de datos
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    # llama al @classmethod de guardado en Usuario
    user_id = User.save(data)
    # almacenar id de usuario en la sesión
    session['user_id'] = user_id
    return redirect("/dashboard")

@app.route('/login', methods=['GET'])
def login2():
    return render_template("login.html")


@app.route('/registro')
def reg():
    return redirect("/")


@app.route('/login', methods=['POST'])
def login():
    # ver si el nombre de usuario proporcionado existe en la base de datos
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # usuario no está registrado en la base de datos
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # si obtenemos False después de verificar la contraseña
        flash("Invalid Email/Password")
        return redirect('/')
    # si las contraseñas coinciden, configuramos el user_id en sesión
    session['user_id'] = user_in_db.id
    # ¡¡¡Nunca renderices en una post!!!
    return redirect("/dashboard")


@app.route('/dashboard')
def dashboard():
    return render_template("index.html")