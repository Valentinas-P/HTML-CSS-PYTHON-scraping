from flask import Flask, template_rendered

app = Flask(__name__)


@app.route("/home")
def default():
    return template_rendered("index.html")
