"""CRUD operations."""

from model import db, User, Artist, Album, Song, Snippet, Snippet_Album, connect_to_db

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

    return artist

def return_all_artists():
    """Return a list of all artists."""

    return Artist.query.all()

def get_artist_by_id(artist_id):
    """Get artist by artist_id."""

    return Artist.query.get(artist_id)

def get_artist_by_name(name):
    """Get artist by name."""

    return Artist.query.filter(Artist.name == name).first()

# ALBUM FUNCTIONS

def create_album(title, thumbnail_path, details, full_lyrics, artist):
    """Create and return a new album."""

    album = Album(title=title,
                thumbnail_path=thumbnail_path,
                details=details,
                full_lyrics=full_lyrics,
                artist=artist)

    db.session.add(album)
    db.session.commit()

    return album

def return_all_albums():
    """Return a list of all albums."""

    return Album.query.all()

def get_album_by_id(album_id):
    """Get album by album_id."""

    return Album.query.get(album_id)

def get_album_by_title(title):
    """Get album by title."""

    return Album.query.filter(Album.title == title).first()

# SONG FUNCTIONS

def create_song(title, album):
    """Create and return a new song."""

    song = Song(title=title, album=album)

    db.session.add(song)
    db.session.commit()

    return song

def get_song_by_id(song_id):
    """Get song by song_id."""

    return Song.query.get(song_id)

# SNIPPET FUNCTIONS

def create_snippet(text, user):
    """Create and return a new snippet."""

    snippet = Snippet(text=text, user=user)

    db.session.add(snippet)
    db.session.commit()

    return snippet

def get_snippet_by_id(snippet_id):
    """Get snippet by snippet_id."""

    return Snippet.query.get(snippet_id)

# SNIPPET_ALBUM FUNCTIONS

def create_snippet_album(snippet, album):
    """Create and return a new snippet_album."""

    snippet_album = Snippet_Album(snippet=snippet, album=album)

    db.session.add(snippet_album)
    db.session.commit()

    return snippet_album

def get_snippet_album_by_id(snippet_album_id):
    """Get snippet by snippet_id."""

    return Snippet.query.get(snippet_album_id)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)