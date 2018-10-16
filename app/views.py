from flask import render_template, request

from app import app

from script.solve import solve

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/q/<question>')
def render_questionfile(question):
    return render_template(question + ".html")

@app.route('/answer/<question>', methods = ["POST"])
def return_answer(question):
	return solve(question, request.form["answer"])
