from flask import Flask, render_template, request, redirect ,session
from datetime import datetime

app = Flask(__name__)  
app.secret_key = "myname"

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    session['strawberry']= request.form['strawberry']
    session['raspberry']= request.form['raspberry']
    session['apple']= request.form['apple']

    session['first_name']= request.form['first_name']
    session['last_name']= request.form['last_name']
    session['student_id']= request.form['student_id']

    session['num_itms'] = int(session['strawberry']) + int (session['raspberry']) + int(session['apple']) 
    now = datetime.now()
    session['d4'] = now.strftime("%d/%m/%Y %H:%M:%S")

    print("Charging :" ,session['first_name'] , session['last_name'] ,  "for: (" , session['num_itms'],")" )
    
    return redirect("/checkout.html")

@app.route('/checkout.html' )         
def theData():
    return render_template("checkout.html")






@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")


    

if __name__=="__main__":   
    app.run(debug=True)    