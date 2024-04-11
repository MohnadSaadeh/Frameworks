from flask import Flask , render_template ,request , redirect , session
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def theFirst():
    return render_template("index.html")

@app.route('/result' , methods = ['POST'])
def theResultPsge():

    session['username'] = request.form['name']
    session['userlocation'] = request.form['location']
    session['userlanguage'] = request.form['language']
    session['usermaassege'] = request.form['message']
    
    return redirect('/info.html'    )  #redirect to the method             # from POST to get                            


@app.route('/info.html')           # method to only do the rindering   insted of render directly
def show_user():
    return render_template("info.html") 




@app.route('/')
def to_the_Root():
    return render_template("index.html" )



if __name__=="__main__":
    app.run(debug=True)