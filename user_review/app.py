#!/usr/bin/env python3
"""use_of_templates/app.py
Develop the power of Flask and Jinja by creating HTML templates,
expending those templates, and pass variable to create dynamic content.
"""

from flask import redirect, url_for, request

import flask  # import the flask library

app = flask.Flask(__name__)  # instantiate a minimal webserver


@app.route('/')  # create the index route
def index():
    # we moved the HTML inside the 'templates/' directory
    # the documentation for the template engine is available here:
    # https://jinja.palletsprojects.com/

    return flask.render_template('index.html')


"""
The function show_review() is called when the user clicks the submit button on the form.

The function show_review() is defined to take one argument, request, which is a dictionary
containing the data that was entered into the form.

The function show_review() extracts the data from the request dictionary and stores it in local
variables.

The function show_review() then renders the success.html template, passing it the local variables as
arguments.

The success.html template displays the data that was entered into the form
:return: The name, review, and score are being returned.
"""


@app.route('/success/', methods=['POST'])
def show_review():
    name = request.form['nm']
    review = request.form['rm']
    score = request.form['sm']
    return flask.render_template(
        'success.html',
        name=name,
        review=review,
        score=score)


"""
It renders the review.html template
:return: The review.html file is being returned.
"""


@app.route('/review/', methods=['POST', 'GET'])
def review():
    return flask.render_template('review.html')


if __name__ == '__main__':  # consider this line as the main
    # start web server in debug mode on port 8080
    app.run('0.0.0.0', 8080, debug=True)
