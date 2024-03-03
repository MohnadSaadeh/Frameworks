from flask import Flask ,render_template , session ,redirect , request , url_for

app =  Flask(__name__)
app.secret_key = 'info user'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html' ,  username=username)
    return redirect(url_for('login'))  #to exequte spesefic Function 

@app.route('/login', methods=["GET" , "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'mohannad' and password == '123456123':
            session['username'] = username 
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return "Invalid Username/Password"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('logged_in',None)
    return redirect(url_for('index'))


if __name__=="__main__":
    app.run(host='192.168.1.12' , port=1200, debug=True)