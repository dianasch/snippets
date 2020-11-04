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
    artist_name = db.Column(db.String(100),
                            nullable = False)
    
    # Method to identify each Artist instance
    def __repr__(self):

        return f"""<Artist user_id={self.artist_id}
                    artist_name={self.artist_name}>"""