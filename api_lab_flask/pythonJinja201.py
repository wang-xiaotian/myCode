#!/usr/bin/env python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hellobasic.html")

@app.route("/<username>")
def hello_name(username):
    return render_template("hellobasic.html", name = username)

# pull in the value of score as an int
@app.route("/scoretest/<int:score>")
def hello_score(score):
    # render the template with the value of score for marks
    # marks is a jinja var in the template
    return render_template("highscore.html", marks = score)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
