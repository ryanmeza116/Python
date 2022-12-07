from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkout', methods = ['POST'])
def checkout():
    print(request.form)
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    order_info = {
        'strawberry': request.form['strawberry'],
        'mango': request.form['mango'],
        'apple': request.form['apple'],
        # Key is fruit name, value comes from form on HTML 
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'student_id':request.form['student_id'],
    }
    total = int(request.form['strawberry']) + int(request.form['mango']) + int(request.form['apple'])

    # HOW CAN I ADD TOGETHER THE TOTAL VALUES AND DISPLAY ON WEBPAGE
    # Why does the values from the index not get saved? 
    print(order_info)
    return render_template('checkout.html', order = order_info, date_time = date_time, total = total)
    # everything in  () gets passed into jinja @ HTML page reffed in route. JINJA looks for variables named 
    # "order" and "date_time"


if __name__=="__main__":
    app.run(debug=True)