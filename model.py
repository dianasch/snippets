"""Models for song snippet app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri='postgresql:///snippet'), echo=True):
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
    __table__name = "users"

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

    # Method to identify each User instance
    def __repr__(self):

        return f"<User user_id={self.human_id} email={self.email}>"


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
    details = db.Column(db.Text)

    # Create table column for full album lyrics as text
    full_lyrics = db.Column(db.Text)

    # Create table column for artist_id as an integer
    # Define foreign key from artists table on artist_id
    # Required field
    artist_id = db.Column(db.Integer,
                        db.ForeignKey("artists.artist_id"),
                        nullable = False)

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
    
    # Create table column for album_id as an integer
    # Define foreign key from albums table on album_id
    # Required field
    album_id = db.Column(db.Integer,
                        db.ForeignKey("albums.album_id"),
                        nullable = False)

    # Create table column for song title as a string
    # Max limit of 50 chars, required field
    title = db.Column(db.String(50),
                        nullable = False)
    
    # Method to identify each Song instance
    def __repr__(self):

        return f"<Song song_id={self.song_id} title={self.title}>"


# if __name__ == '__main__':
#     from server import app

#     connect_to_db(app)
