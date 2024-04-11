from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def sayingHi(name):
    return "Hi " + name + "!"

@app.route('/repeate/<number>/<name>')
def rePeate(number , name):
    num = int(number)
    li = []
    for i in range(0,num):
        li.append(name)
    return li



if __name__=="__main__":
    app.run(debug=True)



