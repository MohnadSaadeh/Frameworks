from flask import Flask ,render_template , session ,redirect , request
import random
from time import gmtime, strftime
app =  Flask(__name__)
app.secret_key = 'my random'

@app.route('/')
def theroot1():
    session['yourgold'] = 0
    session['log_list'] = [] 
    return render_template("index.html")


@app.route('/process_money' , methods = ['POST'])
def earn_take():
    money_earned = 0
    if request.form['which_form'] == 'farm':
            money_earned = int(random.randint(10, 20))
            session['yourgold'] += money_earned

    elif request.form['which_form'] == 'cave':
            money_earned = int(random.randint(10, 20))
            session['yourgold'] += money_earned

    elif request.form['which_form'] == 'house':
            money_earned = int(random.randint(10, 20))
            session['yourgold'] += money_earned

    elif request.form['which_form'] == 'quest':
            money_earned = int(random.randint(-50, 50))
            session['random'] = money_earned
            session['yourgold'] += money_earned
    time = strftime("%Y-%m-%d %H:%M %p , %H:%M:%S ", gmtime())

    if money_earned < 0:
        deal = 'lost'
        session_string = f'you lost {money_earned} in {time}'
    else:
        deal = 'win'
        session_string = f'you won {money_earned} in {time}'
    session['log_list'] += [{'deal': deal, 'session_string': session_string}]
    return redirect("/earn")


@app.route('/earn')
def earn():
    return render_template('index.html')


if __name__=="__main__":
    #app.run(debug=True)
    app.run(debug=True)
