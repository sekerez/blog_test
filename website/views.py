from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

from .models import User, Post
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@views.route("/home/<string:author>")
@login_required
def home(author: str = ""): 
    if author == "":
        posts = Post.query.all()
    else:
        user = User.query.filter_by(username=author).first()
        if not user:
            flash("Invalid Username.")
        posts = user.posts

    return render_template("home.html", 
                           user=current_user,
                           posts=posts,
                           author=author)

