from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def family_table():

    family = [
        {'first_name': 'Ryan', 'last_name': 'Meza'},
        {'first_name': 'Abby', 'last_name': 'Meza'},
        {'first_name': 'Tony', 'last_name': 'Montemurro'},
        {'first_name': 'Tricia', 'last_name': 'Montemurro'},
        {'first_name': 'Karli', 'last_name': 'Montemurro'},
    ]
    return render_template('index.html', family = family)




if __name__ == "__main__":
    app.run(debug=True)