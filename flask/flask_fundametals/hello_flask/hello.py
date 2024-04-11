from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/mohannad')
def comeToMe():
    print("mohannad")
    return "you are in mohannad page"

@app.route('/<name>')
def Aman(name):
    print("yoy are in :", name ,"page")
    return f" you Are in {name} page"

@app.route('/users/<username>/<id>')
def show_user_profile(username,id):
    print(username)
    print(id)
    return "username :" + username + " \n id : " + id




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



