from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

@app.route("/index")
def home():
    return render_template("index.html")

app.run(debug=True)