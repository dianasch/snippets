"""Models for song snippet app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri='postgresql:///snippets', echo=True):
    """Connect Flask app with database."""

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    # Display SQL that is executed
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHECMY_TRACK_MODICIATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


class User(db.Model):
    """A user. Subclass of db.Model."""

    # Set table name as `users` for User objects
    __tablename__ = "users"

    # Create table column for user_id as an integer
    # This is the primary key for users table
    user_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True)

    # Create table column for email as a string
    # Max limit of 100 chars, required field, must be unique
    email = db.Column(db.String(100),
                    nullable = False,
                    unique = True)

    # Create table column for password as a string
    # Max limit of 20 chars, required field
    password = db.Column(db.String(20),
                        nullable = False)

    # snippets = a list of Snippet objects

    # Method to identify each User instance
    def __repr__(self):

        return f"<User user_id={self.user_id} email={self.email}>"


class Artist(db.Model):
    """A music artist. Subclass of db.Model."""

    # Set table name as `artists` for Artist objects
    __tablename__ = "artists"

    # Create table column for artist_id as an integer
    # This is the primary key for artists table
    artist_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True)

    # Create table column for artist name as a string
    # Max limit of 100 chars, required field
    name = db.Column(db.String(100),
                        nullable = False)

    # albums = a list of Album objects
    
    # Method to identify each Artist instance
    def __repr__(self):

        return f"<Artist artist_id={self.artist_id} name={self.name}>"


class Album(db.Model):
    """A music album. Subclass of db.Model."""

    # Set table name as `albums` for Album objects
    __tablename__ = "albums"

    # Create table column for album_id as an integer
    # This is the primary key for albums table
    album_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True)

    # Create table column for album title as a string
    # Max limit of 50 chars, required field
    title = db.Column(db.String(50),
                        nullable = False)

    # Create table column for album thumbnail path as a string
    # Max limit of 2000 chars
    thumbnail_path = db.Column(db.String(2000))

    # Create table column for album details as a text
    # Required field
    details = db.Column(db.Text,
                        nullable = False)

    # Create table column for full album lyrics as text
    # Required field
    full_lyrics = db.Column(db.Text,
                        nullable = False)

    # Create table column for artist_id as an integer
    # Define foreign key from artists table on artist_id
    artist_id = db.Column(db.Integer,
                        db.ForeignKey("artists.artist_id"),
                        nullable = False)

    # Create SQLAlchemy relationship between artists and albums
    artist = db.relationship('Artist', backref='albums')

    # songs = a list of Song objects
    # snippets_albums = a list of Snippets_Albums objects

    # Method to identify each Album instance
    def __repr__(self):

        return f"<Album album_id={self.album_id} title={self.title}>"


class Song(db.Model):
    """A song. Subclass of db.Model."""

    # Set table name as `songs` for Song objects
    __tablename__ = "songs"

    # Create table column for song_id as an integer
    # This is the primary key for songs table
    song_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True)

    # Create table column for song title as a string
    # Max limit of 50 chars, required field
    title = db.Column(db.String(50),
                        nullable = False)

    # Create table column for album_id as an integer
    # Define foreign key from albums table on album_id
    album_id = db.Column(db.Integer,
                        db.ForeignKey("albums.album_id"),
                        nullable = False)

    # Create SQLAlchemy relationship between albums and songs
    album = db.relationship('Album', backref='songs')
    
    # Method to identify each Song instanceq
    def __repr__(self):

        return f"<Song song_id={self.song_id} title={self.title}>"


class Snippet(db.Model):
    """A song snippet generated using a Markov chain. Subclass of db.Model."""

    # Set table name as `snippets` for Snippet objects
    __tablename__ = "snippets"

    # Create table column for snippet_id as an integer
    # This is the primary key for snippets table
    snippet_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True)

    # Create table column for snippet text as text
    # Required field
    text = db.Column(db.Text,
                        nullable = False)

    # Create table column for user_id as an integer
    # Define foreign key from users  table on user_id
    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.user_id"),
                        nullable = False)

    # snippets_albums = a list of Snippets_Albums objects

    # Create SQLAlchemy relationship between users and snippets
    user = db.relationship('User', backref='snippets')
    
    # Method to identify each Snippet instance
    def __repr__(self):

        return f"<Snippet snippet_id={self.snippet_id} text={self.text}>"


class Snippet_Album(db.Model):
    """An intermediate class between snippets and albums.
    Subclass of db.Model."""

    # Set table name as `snippets_albums` for Snippet_Album objects
    __tablename__ = "snippets_albums"

    # Create table column for snippet_album_id as an integer
    # This is the primary key for snippets_albums table
    snippet_album_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True)

    # Create table column for snippet_id as an integer
    # Define foreign key from snippets table on snippet_id
    snippet_id = db.Column(db.Integer,
                        db.ForeignKey("snippets.snippet_id"),
                        nullable = False)

    # Create table column for album_id as an integer
    # Define foreign key from albums table on album_id
    album_id = db.Column(db.Integer,
                        db.ForeignKey("albums.album_id"),
                        nullable = False)

    # Create SQLAlchemy relationship between snippets and snippets_albums
    snippet = db.relationship('Snippet', backref='snippets_albums')

    # Create SQLAlchemy relationship between albums and snippets_albums)
    album = db.relationship('Album', backref='snippets_albums')
    

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
