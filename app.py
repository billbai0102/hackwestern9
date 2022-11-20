from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    return send_from_directory("templates", "index.html")

@app.route('/make')
def make():
    return send_from_directory("templates", "make.html")

@app.route('/style.css')
def style():
    return send_from_directory("templates", "style.css")

@app.route('/script.js')
def script():
    return send_from_directory("templates", "script.js")
