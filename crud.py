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

def get_albums_uploaded_by_user(user_id):
    """Return a list of albums uploaded by user."""

    return get_user_by_id(user_id).albums

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

def create_album(title, thumbnail_path, details, full_lyrics, artist, user_id = None):
    """Create and return a new album."""

    album = Album(title=title,
                thumbnail_path=thumbnail_path,
                details=details,
                full_lyrics=full_lyrics,
                artist=artist,
                user_id=user_id)

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
    """Get album_id by title."""

    return Album.query.filter(Album.title == title).first()

def get_album_title_by_id(album_id):
    """Get album title by album_id."""

    album = get_album_by_id(album_id)

    return album.title

def get_album_thumbnail_by_id(album_id):
    """Get album title by album_id."""

    album = get_album_by_id(album_id)

    return album.thumbnail_path

def get_album_lyrics_by_id(album_id):
    """Get album lyrics by album_id."""

    album = get_album_by_id(album_id)

    return album.full_lyrics

def get_album_lyrics_by_title(title):
    """Get album lyrics by album_id."""

    album = get_album_by_title(title)

    return album.full_lyrics

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

def get_songs_by_album(album_id):
    """Get all songs on an album."""

    return Song.query.filter(Song.album_id == album_id).all()

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

def get_snippets_by_user(user_id):
    """Get snippets saved by user."""

    text = db.session.query(Snippet.text)

    return text.filter(Snippet.user_id == user_id).all()

def get_snippet_text(snippet_id):
    """Get snippet text by snippet_id."""

    text = db.session.query(Snippet.text)

    return text.filter(Snippet.snippet_id == snippet_id).one()

# SNIPPET_ALBUM FUNCTIONS

def create_snippet_album(snippet, album):
    """Create and return a new snippet_album."""

    snippet_album = Snippet_Album(snippet=snippet, album=album)

    db.session.add(snippet_album)
    db.session.commit()

    return snippet_album

def get_snippet_album_by_id(snippet_album_id):
    """Get snippet album by snippet_album_id."""

    return Snippet_Album.query.get(snippet_album_id)


def get_user_album_snippet():
    """Get a dictionary of users with snippets saved by each user sorted by 
    album_id."""

    # Join snippets_albums table with snippets table and albums table
    snippet_album_join = db.session.query(Snippet_Album).options(db.joinedload('album')).options(db.joinedload('snippet')).all()

    # Set variable `user_dict` to empty dictionary
    user_dict = {}

    # Loop through each Snippet_Album object in joined table
    for snippet_album in snippet_album_join:

        # Set variable `user_id` for user_id of Snippet_Album object
        user_id = snippet_album.snippet.user_id

        # Set variable `album_title` to album title for album_id of 
        # Snippet_Album object
        album_title = get_album_title_by_id(snippet_album.album_id)

        # Set variable `album_thumbnail` to album thumbnail for album_id of
        # Snippet_Album object
        album_thumbnail = get_album_thumbnail_by_id(snippet_album.album_id)

        # Set variable `snippet_text` to snippet text for snippet_id
        # Snippet_Album object
        # Cast as string and slice extra parens and quotes off of text
        snippet_text = str(get_snippet_text(snippet_album.snippet_id))[2:-3]

        # Determine if user_id is not already in dictionary
        if user_id not in user_dict:

            # If not, set value of user_id in user_dict to a new dictionary w/
            # key as current album_title
            # value as another dictionary with
            # key as `snippets`,`thumbnail`
            # values as list of snippet_text, thumbnail path

            user_dict[user_id] = {album_title: {"snippets": [snippet_text],
                                                "thumbnail": album_thumbnail}}

        # If user_id is already in dictionary
        else:

            # Determine if dictionary stored at user_id contains
            # current album_title
            if album_title in user_dict[user_id]:
                
                # If so, append current snippet_text to list stored at
                # `snippets` at album_title key
                user_dict[user_id][album_title]["snippets"].append(snippet_text)

            # Otherwise, if current album_title is not in dictionary stored at
            # user_id
            else:

                # Create a new key for current album_title with value as a new
                # dictionary with 
                # key as `snippets`,`thumbnail`
                # values as list of snippet_text, thumbnail path
                user_dict[user_id][album_title] = {"snippets": [snippet_text],
                                                "thumbnail": album_thumbnail}

    return user_dict



if __name__ == '__main__':
    from server import app
    connect_to_db(app)