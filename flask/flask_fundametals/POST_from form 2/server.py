from flask import Flask, render_template , request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")	# notice the 2 new named arguments!

@app.route('/userinfo', methods =['POST'])
def submit_user():
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    return  render_template("theUSER.html" , name_to_template = name_from_form , email_to_template = email_from_form )
    



if __name__=="__main__":
    app.run(debug=True)

