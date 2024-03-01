from flask import Flask ,render_template , session ,redirect , request
import random
app =  Flask(__name__)
app.secret_key = 'my random'


@app.route('/')
def theroot1():
    session['rand'] =  random.randint(1,100)
    session['theGuessed'] = 0
    print(session['rand'])
    return render_template("index.html")

@app.route('/yourguess' , methods = ['POST'])
def theguss():
    session['theGuessed'] = int(request.form['yournu_num']) 
    return redirect('/toredirect')
@app.route('/toredirect')
def theRediFun():
    return render_template("index.html")

@app.route('/clear')
def theclear():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)