from . import db # . stands for the current package
from sqlalchemy.sql import func
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # A model is just a table!
    id = db.Column(db.Integer, primary_key=True) # TODO change to serial
    email = db.Column(db.String(150), unique=True) 
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150)) 
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    posts = db.relationship("Post", backref="user", passive_deletes=True)
    comments = db.relationship("Comment", backref="user", passive_deletes=True)
    # The relationship is necessary to reference posts created by the user
    # backref -> by selecting a post object/row you can use user as an attribute to access user information
    # example: post = Post(...); print(post.user) -> User(...)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey(column="user.id", ondelete="CASCADE"),  # user is lowercase because it's represented as such in the database (?)
        nullable=False
    )
    comments = db.relationship("Comment", backref="post", passive_deletes=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(
        db.Integer,
        db.ForeignKey(column="user.id", ondelete="CASCADE"),
        nullable=False
    )
    post_id = db.Column(
        db.Integer,
        db.ForeignKey(column="post.id", ondelete="CASCADE"),
        nullable=False
    )
