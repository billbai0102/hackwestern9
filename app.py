from flask import Flask, render_template, send_from_directory, request
from cohere_functions import CohereFuncs

app = Flask(__name__)


@app.route('/')
def home():
    return send_from_directory("templates", "index.html")

@app.route('/make')
def make():
    return send_from_directory("templates", "make.html")

@app.route('/results')
def results():
    paramInput = request.args.get('input')
    print("value: " + request.full_path)
    print("param: " + paramInput)

    return send_from_directory("templates", "results.html")

@app.route('/style.css')
def style():
    return send_from_directory("templates", "style.css")

@app.route('/script.js')
def script():
    return send_from_directory("templates", "script.js")

@app.route('/values')
def values():
    paramInput = request.args.get('input')
    print("value: " + paramInput)
    cf = CohereFuncs("JuqpapPUIT9dRAH5a06D4rIj7tTnbWVwY59dY4eC")
    print(cf.get_similar_disease(paramInput))
    return "this is a test response"
