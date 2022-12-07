from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.sighting import Sighting
# import second model

@app.route('/new/sighting')
def new_recipe():
    if "user_id" not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template("new_sighting.html", user = User.get_by_id(data))

@app.route('/create/report', methods = ['POST'])
def create_report():

    if "user_id" not in session:
        return redirect('/logout')
    if not Sighting.validate_sighting(request.form):
        print("VALIDATION FAILED")
        return redirect('/new/sighting')
    data = {
        "location": request.form["location"],
        "what_happened": request.form["what_happened"],
        "date": request.form["date"],
        "number": (request.form["number"]),
        "users_id": session["user_id"]
    }
    Sighting.save(data)
    return redirect('/dashboard')

@app.route('/view/report/<int:id>')
def view_one(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("view_report.html",sighting=Sighting.get_one(data),user=User.get_by_id(user_data))

@app.route('/destroy/report/<int:id>')
def destroy(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Sighting.destroy(data)
    return redirect('/dashboard')

@app.route('/edit/report/<int:id>')
def edit_report(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template('edit.html', user = User.get_by_id(user_data), edit = Sighting.get_one(data))

@app.route('/update/report', methods = ['POST'])
def update_report():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Sighting.validate_sighting(request.form):
        return redirect('/new/sighting')
    data = {
        "location": request.form['location'],
        "what_happened":request.form['what_happened'],
        "date":request.form['date'],
        "number":request.form['number'],
        "id":request.form['id']
    }
    Sighting.update(data)
    return redirect('/dashboard')

