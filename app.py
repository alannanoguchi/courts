from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os


app = Flask(__name__)


host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/courts')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
players = db.players


@app.route('/')
def index():
    """Returns homepage"""
    return render_template('home.html', msg="Courts")


@app.route('/signup')
def signup():
    """Redirects user to sign up page"""
    return render_template("signup.html", msg="Create New Player")


@app.route('/playerhub', methods=['POST'])
def signup_submit():
    """Submit new player."""
    player = {
        'firstname':request.form.get('firstname'),
        'lastname': request.form.get('lastname'),
        'username':request.form.get('username'),
        'city':request.form.get('city'),
        'state':request.form.get('state'),
        'zip':request.form.get('zip'),
        'image':request.form.get('image')
    }
    print(player)
    player_id = players.insert_one(player).inserted_id
    return redirect(url_for('playerhub_show', player_id=player_id))


# This route will show one item
@app.route('/playerhub/<player_id>')
def playerhub_show(player_id):
    """Show the player hub."""
    player = players.find_one({'_id': ObjectId(player_id)})
    return render_template('playerhub_show.html', player=player)


# This route will show one item
@app.route('/playerhub/<player_id>')
def player_show(player_id):
    """Show a single item."""
    player = players.find_one({'_id': ObjectId(player_id)})
    return render_template('playerhub_show.html', player=player)


# This route will take the user to the edit form for the item
@app.route('/playerhub/<player_id>/edit')
def player_edit(player_id):
    """Show the edit form for player"""
    player = players.find_one({'_id': ObjectId(player_id)})
    return render_template('player_edit.html', title='Edit Items', player=player)


# This route will allow the user to post the edited item
@app.route('/playerhub/<player_id>/edited', methods=['POST'])
def player_update(player_id):
    """Submit an edited item."""
    updated_player = {
        'firstname': request.form.get('firstname'),
        'lastname': request.form.get('lastname'),
        'image':request.form.get('image')
    }
    players.update_one(
        {'_id': ObjectId(player_id)},
        {'$set': updated_player})
    
    player = players.find_one({'_id': ObjectId(player_id)})["_id"]
    return redirect(url_for('playerhub_show', player_id=player))

# # This route will allow the user to delete an item
# @app.route('/playerhub/<player.image>/delete', methods=['POST'])
# def image_delete(player_id):
#     """Delete player profile picture"""
#     players.remove({'_id': ObjectId(_id)})
#     return redirect(url_for('home'))





if __name__ == '__main__':
    app.run(debug=True)