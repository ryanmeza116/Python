from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "Ryan"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else :
        session['count'] += 1
    return render_template('index.html')
# Where does the route look for "count" to determine if it is in session. 
@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')
    
if __name__=="__main__":
    app.run(debug=True)