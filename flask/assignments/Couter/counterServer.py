from flask import Flask , render_template ,redirect ,session

app = Flask(__name__)
app.secret_key = 'mohannad'

@app.route('/')
def theroot():
    print(session)
    if 'count' not in session:
        session['count'] = 0 
    session['count'] += 1

    return render_template("index.html")

@app.route('/destroy_session')
def the_new_route():
    session.clear()
    return redirect ('/')   

@app.route('/plus2')
def theplus2():
    session['count']  += 1
    return redirect ('/')



if (__name__) == ("__main__"):
    app.run(debug=True)