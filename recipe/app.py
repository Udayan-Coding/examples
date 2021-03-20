from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template("index.html", name="WORLD!")

@app.route("/about")
def about():
  return render_template("about.html")
