"""Seed file to make sample data for users db."""

from models import Post, User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
alan = User(first_name='Alan', last_name='Alda')
joel = User(first_name='Joel', last_name='Burton')
jane = User(first_name='Jane', last_name='Smith')

# Add new objects to session, so they'll persist
db.session.add(alan)
db.session.add(joel)
db.session.add(jane)

# Add posts
first_post = Post(title='first post',
                  content='This is a first post to test the flask app.', user_id=1)
second_post = Post(title='first post',
                   content='This is a first post to test the flask app.', user_id=2)
third_post = Post(title='first post',
                  content='This is a first post to test the flask app.', user_id=3)
fourth_post = Post(title='second post',
                   content='This is a second post to show multiple posts for one user.', user_id=3)

# Add new posts to session, so they'll persist
db.session.add(first_post)
db.session.add(second_post)
db.session.add(third_post)
db.session.add(fourth_post)

# Commit--otherwise, this never gets saved!
db.session.commit()
