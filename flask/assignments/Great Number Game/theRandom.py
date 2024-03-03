from flask import Flask ,render_template , session ,redirect , request
import random
app =  Flask(__name__)
app.secret_key = 'my random'

@app.route('/')
def theroot1():
    session['rand'] =  int(random.randint(1,100))
    session['theGuessed'] = 0
    session['attempts'] = 0
    session['attemptsUser'] = 10
    print(session['rand'])
    return render_template("index.html")

# Transfrom Data from fromtEnd To BackEnt 
@app.route('/yourguess' , methods = ['POST'])
def theguss():
    session['theGuessed'] = int(request.form['yournu_num']) 
    session['attempts'] += 1 
    session['attemptsUser'] -= 1
    print(session['attempts'])
    return redirect('/toredirect')
@app.route('/toredirect')
def theRediFun():
    return render_template("index.html")
#Transfrom Data from fromtEnd To BackEnt

@app.route('/clear')
def theclear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    #app.run(debug=True)
    app.run(host='192.168.1.12' , port=1200, debug=True)
