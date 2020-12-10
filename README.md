# Hackbright Academy Capstone Project
### Hackbright Academy Full-Stack Software Engineering Program

This web app utilizes Markov chains to generate random song snippets from Taylor Swift's full album lyrics. Non-registered users can view all Taylor Swift albums and create song snippets. Registered users can save their favorite snippets and create snippet mash-ups with their own uploaded albums. Taylor Swift album details are retrieved from the Audio DB API. The most common words in each album are displayed using Chart.js.

### Snippets Demo Video

[![Watch the video](https://img.youtube.com/vi/EMqwaaNgIbo/maxresdefault.jpg)](https://www.youtube.com/watch?v=EMqwaaNgIbo)

## Technologies
* Python
* Flask
* Jinja
* PostgreSQL
* SQLAlchemy
* HTML
* CSS
* Bootstrap
* jQuery
* Javascript (AJAX)

## Overview

### MVP

- WebApp for user to view all Taylor Swift studio albums
- User registration and log-in
- User can view all details for each studio album
- User can create song snippet and save it
- User can view all saved song snippets

### 2.0

- Non-logged in users are able to view albums and create snippets
- Users are able to upload their own album lyrics
- Users are able to create a mash-up snippet with uploaded albums and any Taylor Swift album
- Display saved snippets by album for each user
- Display most common words from each album using Chart.js
- Added log-in and registration security with Flask Login Manager and Werkzeug security

## Features

Users can create an account and log in:

![alt text](https://github.com/dianasch/snippets/blob/main/static/gifs/create-account.gif "Create an account form")
![alt text](https://github.com/dianasch/snippets/blob/main/static/gifs/login.gif "Log in form")

Non-registered users are able to test out the app and view all Taylor Swift studio albums:

![alt text](https://github.com/dianasch/snippets/blob/main/static/gifs/all-albums.gif "Displaying all Taylor Swift albums")

Users who are not logged in can view Taylor Swift album details and create a snippet:

![alt text](https://github.com/dianasch/snippets/blob/main/static/gifs/create-snippet.gif "Creating a snippet on an album details page")

Users who are logged in can save their favorite snippets:

![alt text](https://github.com/dianasch/snippets/blob/main/static/gifs/save-snippet.gif "Saving a snippet")

Saved snippets can be viewed on the "My Snippets" page:

![alt text](https://github.com/dianasch/snippets/blob/main/static/gifs/my-snippets.gif "My snippets page displaying saved snippets")

Users who are logged in can also upload their own album lyrics to create a mash-up snippet with an existing Taylor Swfit album:

![alt text](https://github.com/dianasch/snippets/blob/main/static/gifs/upload-album.gif "Upload album lyrics form")

From there, users can view their uploaded albums and create a mash-up snippet with any Taylor Swift album:

![alt text](https://github.com/dianasch/snippets/blob/main/static/gifs/mash-up.gif "Creating a mash-up snippet from a user-uploaded album")

## Installation

### Requirements

* PostgreSQL
* Python 3.7.3

You are welcome to run this app locally on your own computer. To do so, first clone this repository:

```
$ git clone https://github.com/dianasch/snippets.git
```

Create and activate a virtual environment:

```
$ pip3 install virtualenv
$ virtualenv env
$ source env/bin/activate
```

Install dependencies:

```
(env) $ pip3 install -r requirements.txt
```

Create a secrets.sh file and save your secret key for this app using the following syntax:

```
export SECRET_KEY="your_secret_key"
```

Activate the secrets.sh file in your terminal:

```
(env) $ source secrets.sh
```

Create the database:

```
(env) $ createdb snippets
```

Seed the database:

```
(env) $ python3 model.py
(env) $ python3 seed.py
```

Start the backend server:

```
(env) $ python3 server.py
```

Open a new window and visit this address: http://0.0.0.0:5000/ to view the Snippets app.

## Future Implementation

* Adding Twilio so users can share their favorite snippets
* Creating pagination for users' saved snippets
* Building out more testing for functionality and routes