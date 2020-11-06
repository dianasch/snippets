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
for i in range(len(albums_dict["album"])):

    # Determine if album is a studio album
    if albums_dict["album"][i]["strAlbum"] in studio_albums:


        title = albums_dict["album"][i]["strAlbum"]
        thumbnail_path = albums_dict["album"][i]["strAlbumThumb"]
        details = albums_dict["album"][i]["strDescriptionEN"].split("\n")[0]

        for title in studio_albums:

            file = open(f"data/{title}.txt")
            full_lyrics = file.read()

        db_album = crud.create_album(title, thumbnail_path, details, full_lyrics, crud.get_artist_by_name("Taylor Swift"))
        albums_in_db.append(db_album)





# # Loop through a range the length of number of albums listed in albums_dict
# for i in range(len(albums_dict["album"])):

#     # Determine if album is a studio album
#     if albums_dict["album"][i]["strAlbum"] in studio_albums:

        
#         album_id = albums_dict["album"][i]["idAlbum"]

#         track_url = f"https://theaudiodb.com/api/v1/json/1/track.php?m={album_id}"

#         track_response = requests.get(track_url)

#         track_dict = json.loads(track_response.content)

#         for i in range(len(track_dict["track"])):

#             print(track_dict["track"][i]["strTrack"])

