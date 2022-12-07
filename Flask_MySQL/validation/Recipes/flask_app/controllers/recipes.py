from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipe/<int:id>')
def show_recipe(id):
    # How do i know that the id in the url is stored in ID on line 7
    if 'user_id' not in session:
        return redirect ('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    # data allows us to receive the specific recipe id whereas user_data allows us to receive the specific user id
    return render_template("view_recipe.html",recipe=Recipe.get_one(data),user=User.get_by_id(user_data))

@app.route('/new/recipe')
def new_recipe():
    if "user_id" not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template("new_recipe.html", user = User.get_by_id(data))

@app.route('/create/recipe', methods = ['POST'])
def create_recipe():
    if "user_id" not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe:
        return redirect('/new/recipe')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30": int(request.form["under30"]),
        "date_made": request.form["date_made"],
        "users_id": session["user_id"]
    }
    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/edit/recipe/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template('edit.html', user = User.get_by_id(user_data), edit = Recipe.get_one(data))

@app.route("/update/recipe", methods = ['POST'])
def update():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30": int(request.form["under30"]),
        "date_made": request.form["date_made"],
        "id": request.form['id']
    }
    Recipe.update(data)
    return redirect('/dashboard')

@app.route('/destroy/recipe/<int:id>')
def destroy_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')
