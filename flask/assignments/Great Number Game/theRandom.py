from flask import Flask ,render_template , session ,redirect , request
import random
app =  Flask(__name__)
app.secret_key = 'my random'


@app.route('/')
def theroot1():
    session['rand'] =  random.randint(1,100)
    print(session['rand'])
    return render_template("index.html")


@app.route('/yourguess' , methods = ['POST'])
def theguss():
    session['theGuessed'] = request.form['yournu_num']
    return render_template('index.html')




if __name__=="__main__":
    app.run(debug=True)