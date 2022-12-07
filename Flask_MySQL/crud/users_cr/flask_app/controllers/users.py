from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    print("line 11 - USERS.PY")
    return render_template('index.html', users = User.get_all())

@app.route('/user/new')
def new_user():
    return render_template('new_user.html')

@app.route('/create/user', methods = ['POST'])
def add_user():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/user/show/<int:id>')
def show_user(id):
    # Where is the variable of ID stored? How does it pass into the function? 
    data = {
        "id":id
    }
    return render_template('show_user.html', user = User.get_one(data))

@app.route('/user/delete/<int:id>')
def delete_user(id):
    data = {
        "id":id
    }
    User.delete_one(data)
    return redirect('/')

@app.route('/user/edit/<int:id>')
def display_edit_user(id):
    data = {
        "id":id
    }
    return render_template('edit_user.html', user = User.get_one(data))

@app.route('/user/update', methods = ['POST'])
def edit_user():
    User.update(request.form)
    return redirect('/')
