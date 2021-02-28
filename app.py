"""Blogly application."""

from flask_bootstrap import Bootstrap
from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///blogly"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'phillyflyerswillbechampions'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

bootstrap = Bootstrap(app)
toolbar = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

@app.route('/')
def root():
    """Homepage redirects to list of users."""

    return redirect("/users")

@app.route('/users')
def users_index():
    """Render a page with a list of all users"""

    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users/index.html', users=users)