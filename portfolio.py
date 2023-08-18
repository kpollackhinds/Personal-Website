from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/aboutme")
def about_me():
    return render_template("aboutme.html")


if __name__ == "__main__":
    app.run(debug=True)