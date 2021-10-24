from . import db # . stands for the current package
from sqlalchemy.sql import func
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # A model is just a table!
    id = db.Column(db.Integer, primary_key=True) # TODO change to serial
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150)) # TODO include hash
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

