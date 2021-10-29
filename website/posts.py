from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from .models import Post
from . import db

posts = Blueprint("posts", __name__)

@posts.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get("text")
        if not text:
            flash("Post cannot be empty", category="error")
        else:
            new_post = Post(
                text=text,
                user_id=current_user.id
            )
            db.session.add(new_post)
            db.session.commit()
            flash("Post created!", category="success")

    return render_template("create_post.html", user=current_user)


@posts.route("/delete-post/<int:id>", methods=["GET"])
@login_required
def delete_post(id: int):
    """
    Deletes a post, duh.
    """
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash("Post cannot be deleted.", category="error")
    elif current_user.id != post.user_id:
        flash("Users can only delete their own posts.", category="error")
    else:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted!", category="success")

    return redirect(url_for("views.home"))