from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    """Returns homepage"""
    return render_template('home.html', msg="Courts")


@app.route('/signup')
def signup():
    """Redirects user to sign up page"""
    return render_template("signup.html", msg="Create New Player")