from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os


app = Flask(__name__)


host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/courts')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
items = db.items

@app.route('/')
def index():
    """Returns homepage"""
    return render_template('home.html', msg="Courts")


@app.route('/signup')
def signup():
    """Redirects user to sign up page"""
    return render_template("signup.html", msg="Create New Player")





if __name__ == '__main__':
    app.run(debug=True)