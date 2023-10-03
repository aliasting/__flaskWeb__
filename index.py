from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, Flask!</h1><h2>Flask2級!</h2><p>這是段落1111</p>"

@app.route("/hello_world")
def hello_world():
    return "<h1>HEllo! World.</h1>"

