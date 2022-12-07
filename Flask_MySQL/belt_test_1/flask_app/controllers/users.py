from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.sighting import Sighting
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/register_render')
def register():
    return render_template('/register.html')

@app.route('/login_render')
def login():
    return render_template('/login.html')

@app.route('/')
def entry():
    return redirect('/login_render')

@app.route('/login', methods = ['POST'])
def user_login():
    user = User.get_by_email(request.form)
    print('***')
    print('USER IS', user)
    print('***')
    if not user:
        flash("Invalid Email","login")
        return redirect('/login_render')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/login_render')
    session['user_id'] = user.id
    return redirect('/dashboard')
    # If template after login != dashboard.html // page wont run. change accordingly


@app.route('/register',methods=['POST'])
def user_register():
    print('MADE IT TO REGISTER')
    if not User.validate_register(request.form):
        return redirect('/register_render')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect('/dashboard')
    # If template after login != dashboard.html // page wont run. change accordingly

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        
        return redirect('/logout')
    data ={
        'id': session['user_id']
        
    }
    print("SIGHTING GET ALL",Sighting.get_all())
    return render_template("dashboard.html",user=User.get_by_id(data),sightings = Sighting.join_all())
    # current dashboard only displays user

# ** all lines above copied and pasted from Login/Registration 

@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/')