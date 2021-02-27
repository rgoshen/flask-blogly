"""Blogly application."""

from flask_bootstrap import Bootstrap
from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
# from models import db, connect_db, User

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///blogly"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'phillyflyerswillbechampions'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

bootstrap = Bootstrap(app)
toolbar = DebugToolbarExtension(app)


# connect_db(app)
# db.create_all()
