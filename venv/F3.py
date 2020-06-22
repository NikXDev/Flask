from flask import Flask, render_template
# Static Files, HTTP Methods, HTML Templates
app  = Flask(__name__)

@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)