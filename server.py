"""Server for song snippet app."""

from flask import (Flask, render_template, request, flash, session,
                    redirect, jsonify)
from jinja2 import StrictUndefined
import requests
import os

from model import connect_to_db
import crud
import markov

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def get_homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/albums')
def show_all_albums():
    """View all albums."""

    albums = crud.return_all_albums()

    return render_template('all_albums.html', albums=albums)

@app.route('/albums/<album_id>')
def show_album_details(album_id):
    """Show details on specific albums."""

    album = crud.get_album_by_id(album_id)
    songs = crud.get_songs_by_album(album_id)

    return render_template('album_details.html', album=album,
                                                songs=songs)

@app.route('/albums/<album_id>/snippet')
def create_snippet(album_id):

    title = crud.get_album_title_by_id(album_id)
    lyrics = crud.get_album_lyrics_by_id(album_id)

    chains = markov.make_chains(lyrics)
    snippet = markov.make_text(chains)

    return render_template('snippet.html', title=title,
                                        snippet=snippet)

@app.route('/users', methods = ['POST'] )
def register_user():
    """Get inputs from create account form."""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)

    if user == None:
        crud.create_user(email, password)
        flash('Account created! You can now log in.')
    else:    
        flash('Email already exists. Try again.')

    return redirect('/')

@app.route('/login', methods = ['POST'])
def log_in():
    """Gets input from log-in and checks to see if emails and passwords
    match."""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)

    if email == user.email and password == user.password:
        session['user'] = user.user_id
        flash('Logged in!')
    else:
        flash('Email and password do not match.')
    
    return redirect('/')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")