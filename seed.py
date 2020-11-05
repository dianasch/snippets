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

# Loop through a range the length of number of albums listed in albums_dict
for i in range(len(albums_dict["album"])):

    # Determine if album is a studio album
    if albums_dict["album"][i]["strAlbum"] in studio_albums:

        # Print album title
        print(albums_dict["album"][i]["strAlbum"])



