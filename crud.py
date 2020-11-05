"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

# USER FUNCTIONS

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def return_all_users():
    """Return a list of all users."""

    return User.query.all()

def get_user_by_id(user_id):
    """Get user by user_id."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Get user by email."""

    return User.query.filter(User.email == email).first()

# ARTIST FUNCTIONS

def create_artist(name):
    """Create and return a new artist."""

    artist = Artist(name=name)

    db.session.add(artist)
    db.session.commit()

    return user

def return_all_artists():
    """Return a list of all artists."""

    return Artist.query.all()

def get_artist_by_id(artist_id):
    """Get artist by artist_id."""

    return Artist.query.get(artist_id)

# ALBUM FUNCTIONS

