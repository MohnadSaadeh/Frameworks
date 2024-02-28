from flask import Flask ,render_templates
app =  Flask(__name__)

@app.route('/')
def theroot1():
    return render_templates("")

if __name__=="__main__":
    app.run(debug=True)