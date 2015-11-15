"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, render_template, redirect
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello(name=None):
    """Return a friendly HTTP greeting."""
    return render_template('hello.html', name=name)

@app.route('/resume')
def resume():
    return redirect("https://www.dropbox.com/s/3zj5g0iykv9a651/Xinhe_Ren_Resume.pdf?dl=0")


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
