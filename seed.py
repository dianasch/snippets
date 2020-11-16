"""Script to seed database."""

import os
import json
import requests

import crud
import model
import server

os.system('dropdb snippets')
os.system('createdb snippets')

model.connect_to_db(server.app)
model.db.create_all()

# Add Taylor Swift to snippets db
crud.create_artist("Taylor Swift")

# URL from The Audio DB API containing info on Taylor Swift albums
albums_url = "https://www.theaudiodb.com/api/v1/json/1/searchalbum.php?s=taylor_swift"

# Response object from URL
albums_response = requests.get(albums_url)

# Convert response object to dictionary
albums_dict = json.loads(albums_response.content)

# Set of Taylor Swift's studio albums
studio_albums = set(["folklore", "Lover", "reputation", "1989",
                    "Red", "Speak Now", "Fearless", "Taylor Swift"])


albums_in_db = []



# Loop through a range the length of number of albums listed in albums_dict
for album in albums_dict["album"]:

    # Determine if album is a studio album
    if album["strAlbum"] in studio_albums:

        # Pull title, thumbnail_path, and details from API
        title = album["strAlbum"]
        thumbnail_path = album["strAlbumThumb"]
        details = album["strDescriptionEN"].split("\n")[0]

        # Pull .txt files of full lyrics for each album from data folder
        file = open(f"data/{title}.txt")
        full_lyrics = file.read()

        # Add each studio album to albums table db
        # Link to artist Taylor Swift in db
        db_album = crud.create_album(title,
                                    thumbnail_path,
                                    details,
                                    full_lyrics,
                                    crud.get_artist_by_name("Taylor Swift"))

        # Add each studio album to albums_in_db list
        albums_in_db.append(db_album)



        # Pull API's album id for each studio album
        album_id = album["idAlbum"]

        # URL from The Audio DB API containing track listings for each album
        track_url = f"https://theaudiodb.com/api/v1/json/1/track.php?m={album_id}"

        # Response object from URL
        track_response = requests.get(track_url)

        # Convert response object to dictionary
        track_dict = json.loads(track_response.content)

        # Loop through a range the length of number of albums
        # listed in track_dict
        for track in track_dict["track"]:

            # Add each song to songs table in db
            # Pull album title from API to link to album in db
            crud.create_song(track["strTrack"],
                            crud.get_album_by_title(track["strAlbum"]))

