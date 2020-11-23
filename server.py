"""Server for song snippet app."""

from flask import (Flask, render_template, request, flash, session,
                    redirect, jsonify)
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from jinja2 import StrictUndefined
from urllib.parse import urlparse, urljoin
import random
import requests
import os

from model import connect_to_db
import crud
import markov

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.jinja_env.undefined = StrictUndefined

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def get_homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/albums')
def show_all_albums():
    """View all albums."""

    albums = crud.return_all_albums()

    # If user is not logged in, only show Taylor Swift albums
    ts_albums = albums[:8]

    # If user is logged in
    if current_user:
        
        # Show albums uploaded by user as well
        user_albums = crud.get_albums_uploaded_by_user(current_user.get_id())

    # Otherwise, if user is not logged in, there are no user_albums
    else:

        user_albums = []

    return render_template('all_albums.html', ts_albums=ts_albums, user_albums=user_albums)

@app.route('/albums/<album_id>')
def show_album_details(album_id):
    """Show details on specific albums."""

    album = crud.get_album_by_id(album_id)
    songs = crud.get_songs_by_album(album_id)
    lyrics = crud.get_album_lyrics_by_id(album_id)
    chart_data = markov.most_common(lyrics)

    return render_template('album_details.html', album=album,
                                                songs=songs,
                                                album_id=album_id,
                                                chart_data=chart_data)

@app.route('/albums/<album_id>/snippet', methods = ['GET'])
def create_snippet(album_id):
    """Create and display Markov song snippet from album lyrics."""

    album = crud.get_album_by_id(album_id)
    title = crud.get_album_title_by_id(album_id)

    # User selection from drop-down menu for Taylor Swift album
    ts_album = request.args.get("taylor-swift-album")

    # Get full lyrics for the current album id page
    lyrics = crud.get_album_lyrics_by_id(album_id)

    # Determine if there is a value for ts_album
    # If so, user is on a user album page to make a mash-up
    if ts_album:

        # Determine if user selection from drop-down menu is a random
        # Taylor Swift album
        if ts_album == "9":

            # If so, get full lyrics for a random Taylor Swift album
            ts_lyrics = crud.get_album_lyrics_by_id(random.randint(1, 8))

        # Or if user selection is a specific Taylor Swift album
        else:

            # Get full lyrics for specific Taylor Swift album
            ts_lyrics = crud.get_album_lyrics_by_id(int(ts_album))

    # Otherwise, there is no ts_album because we are on a Taylor Swift
    # album page
    else:

        # Set `ts_lyrics` to an empty string
        ts_lyrics = ""

    # Create Markov chains from full album lyrics
    chains = markov.make_chains(lyrics + ts_lyrics)

    # Create song snippet from `chains`
    snippet = markov.make_text(chains)

    # Store song snippet in session
    session['snippet'] = snippet

    return render_template('snippet.html', title=title, snippet=snippet, album=album)

@app.route('/albums/<album_id>/snippet/save')
def save_snippet(album_id):
    """Save song snippet to database."""

    album = crud.get_album_by_id(album_id)
    snippet = session['snippet']


    if current_user:
        db_snippet = crud.create_snippet(snippet, crud.get_user_by_id(current_user.get_id()))
        snippet_album = crud.create_snippet_album(db_snippet, album)
        flash('Snippet saved!')
    else:
        flash('Log in to save your snippet!')

    return redirect(f"/all-users/{current_user.get_id()}")

@app.route('/user-album-form')
def show_user_upload_form():
    """Display user form to upload new album."""

    return render_template('user_album_form.html')

@app.route('/user-album-upload', methods = ['POST'])
def add_user_upload_to_db():
    """Adds new album to db from user input form."""

    # Get user input from album upload form
    artist = request.form.get('artist')
    title = request.form.get('title')
    thumbnail = request.form.get('thumbnail')
    description = request.form.get('description')
    lyrics = request.form.get('lyrics')
    user_id = current_user.get_id()

    # Check if artist is already in db
    try:
        
        crud.get_artist_by_name(artist)

    # If artist not in db, getting artist will return a KeyError
    except KeyError:

        # Add artist to db
        crud.create_artist(artist)

    # Add album to db
    crud.create_album(title,
                    thumbnail,
                    description,
                    lyrics,
                    crud.get_artist_by_name(artist),
                    user_id)
    flash("Album saved!")

    return redirect('/albums')

@app.route('/all-users')
def show_all_users():
    """View all users."""

    users = crud.return_all_users()

    return render_template('all_users.html', users=users)

@app.route('/all-users/<user_id>')
def user_details(user_id):
    """Show user detail page with favorite song snippets."""

    user = crud.get_user_by_id(user_id)
    user_dict = crud.get_user_album_snippet()

    # user_dict contains Snippet_Album items
    # If user has not saved any snippets yet, user will not be in user_dict
    # Try checking if user is in user_dict
    try:

        snippets = user_dict[int(user_id)]

    # If user is not in user_dict, attempting to look up user will result
    # in a KeyError
    except KeyError:

        # If user is not in user_dict, there are no snippets saved
        # Set `snippets` to empty list
        snippets = []

    return render_template('user_details.html', user=user,
                                                snippets=snippets)

@app.route('/users', methods = ['POST'] )
def register_user():
    """Get inputs from create account form."""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)
    print(user)
    if user == None:
        crud.create_user(email, password)
        flash('Account created! You can now log in.')
    else:    
        flash('Email already exists.')

    return redirect('/')

@login_manager.user_loader
def load_user(user_id):

    return crud.get_user_by_id(user_id)

# Flask snippet to check for a safe URL
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

@app.route('/login', methods = ['POST'])
def log_in():
    """Log a user in."""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)

    if user:

        if password == user.password:
            login_user(user)
            flash('Logged in!')

            next = request.args.get('next')

            if not is_safe_url(next):
                return abort(400)

            return redirect(next or '/')

        else:
            flash('Email and password do not match.')
    
    else:
        flash('There is no account associated with this email. Please create an account!')

    return redirect('/')

@app.route('/logout', methods = ['POST'])
@login_required
def log_out():
    """Log a user out."""

    logout_user()
    flash("Logged out!")

    return redirect('/')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")