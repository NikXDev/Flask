from flask import Flask

app  = Flask(__name__)  # app is like a flask object, We add name to route path the app

@app.route("/") # @ signifies a decorator - a way to wrap a function and modifying its behaviour
def index():
    return "Hello, This Is The Home Page"

@app.route("/tuna")
def tuna():
    return "<h2>Tuna Is Good..!!!!!</h2>"

@app.route("/profile/<username>")
def profile(username):
    return "Hey There %s" %username

@app.route("/post/<int:postid>")
def post(postid):
    return "Your PostID is %s" %postid

if __name__ == "__main__":
    app.run(debug=True) # basically start the app
