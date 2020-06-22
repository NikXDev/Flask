from flask import Flask, render_template
# Mapping Multiple URLs, Passing Objects Into Template
app  = Flask(__name__)

@app.route("/")
@app.route("/<user>")
def index(user=None):
    return render_template("user.html", user=user)

@app.route("/shopping")
def shopping():
    food = ["Cheese", "Tuna", "Pork", "Toothpaste"]
    return render_template("shopping.html", food=food)

if __name__ == "__main__":
    app.run()