from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.tree import Tree
# import second model

@app.route('/create/tree')
def plant_tree():
    if "user_id" not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template("plant_tree.html", user = User.get_by_id(data))

@app.route('/plant/tree', methods = ['POST'])
def create_report():

    if "user_id" not in session:
        return redirect('/logout')
    if not Tree.validate_tree(request.form):
        print("VALIDATION FAILED")
        return redirect('/create/tree')
    data = {
        "species": request.form["species"],
        "location": request.form["location"],
        "reason": request.form["reason"],
        "date_planted": request.form["date_planted"],
        "users_id": session["user_id"]
    }
    Tree.save(data)
    return redirect('/dashboard')

@app.route('/view/trees')
def view_trees():
    if 'user_id' not in session:
        return redirect('/logout')
    user_data = {
        "id": session['user_id']
    }
    return render_template("users_trees.html",trees= Tree.join_all(),user=User.get_by_id(user_data))

@app.route('/delete/tree/<int:id>')
def destroy(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Tree.destroy(data)
    return redirect('/view/trees')

@app.route('/edit/tree/<int:id>')
def edit_report(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template('edit_tree.html', user = User.get_by_id(user_data), tree = Tree.get_one(data))

@app.route('/replant/tree', methods = ['POST'])
def update_report():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Tree.validate_tree(request.form):
        return redirect('/view/trees')
    data = {
        "species": request.form["species"],
        "location": request.form["location"],
        "reason": request.form["reason"],
        "date_planted": request.form["date_planted"],
        "users_id": session["user_id"]
    }
    Tree.update(data)
    return redirect('/dashboard')

@app.route('/view/tree/<int:id>')
def view_one(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("view_tree.html", tree=Tree.get_user_and_tree(data), user=User.get_by_id(user_data))
