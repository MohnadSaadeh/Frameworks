from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def chech1():
    return render_template("index.html")

@app.route('/<x>')
def chech2(x):
    return render_template("index2.html" , var = int(x) )
    
@app.route('/<x>/<y>')
def chech3(x ,y):
    return render_template("index3.html" , varx = int(x) , vary = int(y) )

@app.route('/<x>/<y>/<color1>/<color2>')
def chech4(x ,y , color1 ,color2):
    return render_template("index4.html" , varx = int(x) , vary = int(y) , col1 = color1 , col2 = color2  )





if __name__=="__main__":
    app.run(debug=True)