from flask import Flask , render_template
app = Flask(__name__)

@app.route('/play')
def hello_world():
    return render_template('index.html')

@app.route('/play/<num>')
def hello_world2(num):
    return render_template('index2.html' , num_divs = int(num) )

@app.route('/play/<num>/<color>')
def hello_world3(num , color):
    return render_template('index3.html' , num_divs = int(num) , the_color = color )


if __name__=="__main__":
    app.run(debug=True)