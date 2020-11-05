"""Server for song snippet app."""

from flask import (Flask, render_template, request, flash, session,
                    redirect)
from model import connect_to_db

from jinja2 import StrictUndefined

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")