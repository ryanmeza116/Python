from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default_board():
    return render_template('checkers.html')




























if __name__ == "__main__":
    app.run(debug=True)